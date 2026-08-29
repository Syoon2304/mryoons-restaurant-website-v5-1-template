from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTests(unittest.TestCase):
    def test_rollback_detects_the_staged_restore_against_head(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "rollback-website.yml").read_text(encoding="utf-8")
        self.assertIn("git diff --quiet HEAD -- public", workflow)
        self.assertNotIn("git diff --quiet -- public", workflow)


if __name__ == "__main__":
    unittest.main()
