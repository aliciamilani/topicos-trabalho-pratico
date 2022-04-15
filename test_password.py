import unittest
from password_validator import validator

class RoteiroTesteFuncional(unittest.TestCase):
    def test_ct01(self):
        res = validator("L!3C9@")
        self.assertEqual(res, 'invalido')

    def test_ct02(self):
        res = validator("L!3C9@M")
        self.assertEqual(res, 'valido')

    def test_ct03(self):
        res = validator("L!3C9@5tRs7_49*")
        self.assertEqual(res, 'valido')

    def test_ct04(self):
        res = validator("L!3C9@5tRs7_49*#")
        self.assertEqual(res, 'invalido')

    def test_ct05(self):
        res = validator("9kgz*q5(l1")
        self.assertEqual(res, 'invalido')

    def test_ct06(self):
        res = validator("9KGz*q5(l1")
        self.assertEqual(res, 'valido')

    def test_ct07(self):
        res = validator("9KGZ*q5(l1")
        self.assertEqual(res, 'valido')

    def test_ct08(self):
        res = validator("6H)lwb_K")
        self.assertEqual(res, 'invalido')

    def test_ct09(self):
        res = validator("6H)lwb_K8")
        self.assertEqual(res, 'valido')

    def test_ct10(self):
        res = validator("6H)lwb_7K8")
        self.assertEqual(res, 'valido')

    def test_ct11(self):
        res = validator("j8Dr-0fP")
        self.assertEqual(res, 'invalido')

    def test_ct012(self):
        res = validator("j8Dr-0fP@")
        self.assertEqual(res, 'valido')
    
    def test_ct013(self):
        res = validator("j%8Dr-0fP@")
        self.assertEqual(res, 'valido')

    def test_ct014(self):
        res = validator("1!UY_9 0#m")
        self.assertEqual(res, 'invalido')

    def test_ct015(self):
        res = validator("$J55mQ+B")
        self.assertEqual(res, 'invalido')

    def test_ct016(self):
        res = validator("8!3C9@Mp")
        self.assertEqual(res, 'valido')

if __name__ == "__main__":
    unittest.main()