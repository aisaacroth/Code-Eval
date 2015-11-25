/*
 * bit-position.h - The header file for bit-position.c
 *
 * Author: Alexander Roth
 * Date:   2015-11-25
 */

#ifndef __BIT_POSITION_H__
#define __BIT_POSITION_H__

char *dec_to_bin(int num);
int check_bits(char *num, int pos_1, int pos_2);
void print_match(int check);

#endif
