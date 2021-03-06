﻿Block Reverse Kata
----------------------

For an array of integers greater than or equal to -1, we define a block as a slice of the array consisting of adjacent non-negative integers. For example, the array [ 1, 2, 3, -1, 4, 5, -1, 6, -1, -1 ] contains three blocks:

    block 1 = 1, 2, 3
    block 2 = 4, 5
    block 3 = 6

Write a function for reversing the array, but not reversing the content of the blocks themselves.

Some example (and test cases):

    block_reverse( [ 1, 2, 3 ] ) = [ 1, 2, 3 ]
    block_reverse( [ -1 ] = [ -1 ]
    block_reverse( [ 1, 2, -1, 3] ) = [ 3, -1, 1, 2 ]
    block_reverse( [ -1, -1, 1, 2, 3, -1, 2, 4, 6, 8 ] ) = [ 2, 4, 6, 8, -1, 1, 2, 3, -1, -1 ]
