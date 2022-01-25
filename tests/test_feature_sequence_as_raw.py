import os
import pytest
from pyfaidx import Faidx, Fasta
from unittest import TestCase

path = os.path.dirname(__file__)
os.chdir(path)

class TestFeatureSequenceAsRaw(TestCase):
    def setup_method(self):
        pass

    def teardown_method(self):
        try:
            os.remove('data/genes.fasta.fai')
        except EnvironmentError:
            pass  # some tests may delete this file

    def test_as_raw_false(self):
        fasta = Fasta('data/genes.fasta')
        expect = 'TTGAAGATTTTGCATGCAGCAGGTGCGCAAGGTGAAATGTTCACTGTTAAA'.lower()
        result = fasta['gi|557361099|gb|KF435150.1|'][100-1:150].seq.lower()
        assert result == expect

    def test_as_raw_true(self):
        fasta = Fasta('data/genes.fasta', as_raw=True)
        expect = 'TTGAAGATTTTGCATGCAGCAGGTGCGCAAGGTGAAATGTTCACTGTTAAA'.lower()
        result = fasta['gi|557361099|gb|KF435150.1|'][100-1:150].lower()
        assert result == expect

    @pytest.mark.xfail(raises=AttributeError)
    def test_as_raw_false_error(self):
        fasta = Fasta('data/genes.fasta')
        result = fasta['gi|557361099|gb|KF435150.1|'][100-1:150].lower()

    @pytest.mark.xfail(raises=AttributeError)
    def test_as_raw_true_error(self):
        fasta = Fasta('data/genes.fasta', as_raw=True)
        result = fasta['gi|557361099|gb|KF435150.1|'][100-1:150].seq.lower()

    def test_as_raw_type_when_blen_lt_0(self):
        fasta = Fasta('data/genes.fasta', as_raw=True)
        expect = ''
        result = fasta.faidx.fetch('gi|557361099|gb|KF435150.1|', 10, 0)
        assert result == expect
