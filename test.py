import unittest
from index import reconcile

class TestReconcile(unittest.TestCase):
    def test_reconcile(self):
        # Prepare test data
        source_file = 'tests/source.csv'
        target_file = 'tests/target.csv'
        output_file = 'tests/reconciliation_report.csv'
        compare_columns = ['Date', 'Amount']
        
        # Run reconciliation
        missing_in_target, missing_in_source, discrepancies = reconcile(source_file, target_file, output_file, compare_columns)
        
        # Check results
        self.assertEqual(missing_in_target, 1)
        self.assertEqual(missing_in_source, 1)
        self.assertEqual(discrepancies, 1)

if __name__ == '__main__':
    unittest.main()
