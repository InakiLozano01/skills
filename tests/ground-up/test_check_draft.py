"""Each fail fixture is a real past mistake from a ground-up run; each pass fixture is approved text."""
import pathlib, subprocess, sys, unittest

HERE = pathlib.Path(__file__).parent
SCRIPT = HERE.parents[1] / "skills" / "ground-up" / "scripts" / "check_draft.py"
EXPECT = {
    "fail-lena-2026-11-03.txt": ["spanglish", "questions"],
    "fail-fin-avances-0145.txt": ["dash", "spanglish", "voseo"],
    "fail-crm-precios-374b.txt": ["voseo"],
}


def run(name, *flags):
    return subprocess.run([sys.executable, str(SCRIPT), *flags, str(HERE / "fixtures" / name)],
                          capture_output=True, text=True)


class CheckDraft(unittest.TestCase):
    def test_real_mistakes_fail(self):
        for name, rules in EXPECT.items():
            out = run(name)
            self.assertEqual(out.returncode, 1, name)
            for rule in rules:
                self.assertIn(f"ERROR line", out.stdout)
                self.assertRegex(out.stdout, rf"ERROR line \d+ \[{rule}\]", f"{name}: {rule}")

    def test_backstage_is_flagged(self):
        out = run("fail-cargocheck-example-before.txt")
        self.assertIn("[backstage] 'subagentes'", out.stdout)
        self.assertIn("[backstage] 'worktrees'", out.stdout)

    def test_template_phrasing_is_flagged(self):
        out = run("fail-lena-rewrite-out11.txt")
        self.assertRegex(out.stdout, r"\[template\] 'puerta de dos sentidos")

    def test_skill_vocabulary_is_flagged(self):
        out = run("fail-lena-rewrite-terra-out11.txt")
        self.assertIn("[backstage] 'puerta irreversible'", out.stdout)

    def test_word_budget_is_measured(self):
        out = run("fail-lena-rewrite-out11.txt", "--original", str(HERE / "fixtures" / "orig-lena-2026-11-03.txt"))
        self.assertRegex(out.stdout, r"\[budget\] \d+ palabras contra \d+ del original \(1\.\d\dx\)")

    def test_estimate_refusal_is_flagged(self):
        out = run("fail-romina-terra-out12.txt")
        self.assertIn("[estimate]", out.stdout)
        out = run("fail-fin-sin-recalculo-0145.txt")
        self.assertIn("[estimate]", out.stdout)

    def test_double_numbering_is_flagged(self):
        out = run("fail-lena-rewrite-terra-out12.txt")
        self.assertIn("[numbering]", out.stdout)

    def test_option_tautology_is_flagged(self):
        for name in ["fail-lena-rewrite-terra-out12.txt", "fail-lena-rewrite-terra-out13.txt"]:
            self.assertIn("[tautology]", run(name).stdout, name)

    def test_owner_budget_is_tighter(self):
        orig = str(HERE / "fixtures" / "orig-lena-2026-11-03.txt")
        out = run("fail-lena-rewrite-luna-out15.txt", "--original", orig, "--owner")
        self.assertRegex(out.stdout, r"ERROR line 0 \[budget\]")
        out = run("fail-lena-rewrite-luna-out15.txt", "--original", orig)
        self.assertNotRegex(out.stdout, r"ERROR line 0 \[budget\]")

    def test_long_message_fails_and_its_accepted_cut_passes(self):
        """A 1090-word Slack message got "¿lo puedes hacer más corto?"; the 499-word cut was accepted."""
        out = run("fail-security-status-1105.masked.txt")
        self.assertRegex(out.stdout, r"ERROR line 0 \[size\] mensaje de 1090 palabras")
        out = run("pass-security-status-short-1105.masked.txt")
        self.assertNotIn("[size]", out.stdout)

    def test_rewrite_and_document_have_no_message_ceiling(self):
        orig = str(HERE / "fixtures" / "orig-lena-2026-11-03.txt")
        self.assertNotIn("[size]", run("fail-lena-rewrite-out11.txt", "--original", orig).stdout)
        doc = "# Informe\n\n" + "palabra " * 900
        out = subprocess.run([sys.executable, str(SCRIPT)], input=doc, capture_output=True, text=True)
        self.assertNotIn("[size]", out.stdout)

    def test_approved_text_passes(self):
        out = run("pass-fin-aprobado.txt")
        self.assertEqual(out.returncode, 0, out.stdout)


if __name__ == "__main__":
    unittest.main()
