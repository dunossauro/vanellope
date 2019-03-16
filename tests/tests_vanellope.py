from unittest import TestCase, mock
from vanellope import chunks, rotate_blocks, remove_blocks


class TestChunks(TestCase):
    def tests_chunks_should_resize_even_blocks(self):
        self.assertEqual(chunks([1, 2, 3], 2), [[1, 2], [3]])

    def tests_chunks_should_resize_100_elements_in_10_blocks(self):
        block = list(range(1, 101))
        expected_size = 10
        self.assertEqual(len(chunks(block, 10)), expected_size)


class TestRotateBlocks(TestCase):
    @mock.patch('vanellope.vanellope.choice', return_value=1)
    def test_rotate_block_should_return_inversed_first_block(self, m_choice):
        block = [[1], [2], [3], 4]
        expected = [[2], [1], [3], 4]
        self.assertEqual(rotate_blocks(block, 1), expected)


class TestRemoveBlocks(TestCase):
    def test_remove_blocks_should_remove_2_blocks(self):
        block = [1, 2, 3]
        expected_size = 1
        self.assertEqual(len(remove_blocks(block, 2)), expected_size)
