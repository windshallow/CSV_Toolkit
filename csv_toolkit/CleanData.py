# -*- coding: utf-8 -*-

import csv


def eliminate_repeated_row(in_file, out_file):
    """ 消除重复的行 """
    with open(in_file, 'rb') as in_file, open(out_file, 'wb')as out_file:
        seen = set()
        for line in in_file:
            # print line
            if line in seen:
                continue

            seen.add(line)
            out_file.write(line)

# eliminate_repeated_row('/Users/admin/Desktop/data.csv', '/Users/admin/Desktop/data_2.csv')


def dict_same_value(original_dict):  # seem no use
    new_dict = {}
    for k, v in original_dict.iteritems():
        new_dict.setdefault(v, []).append(k)
    return new_dict
