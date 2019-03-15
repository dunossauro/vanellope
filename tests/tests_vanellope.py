from unittest import TestCase, mock
from vanellope import chunks, rotate_blocks


class TestChunks(TestCase):
    def tests_chunks_should_resize_even_blocks(self):
        self.assertEqual(chunks([1, 2, 3], 2), [[1, 2], [3]])


class TestRotateBlocks(TestCase):
    @mock.patch('vanellope.vanellope.choice', return_value=1)
    def test_rotate_block_should_return_inversed_first_block(self, m_choice):
        block = [[1], [2], [3], 4]
        expected = [[2], [1], [3], 4]
        self.assertEqual(rotate_blocks(block, 1), expected)
