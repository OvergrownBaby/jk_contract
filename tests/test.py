# -*- coding: GBK -*-

import regex
from jk_contract import Contract
from jk_contract import Contracts

# contract = Contract('/Users/andy/Desktop/work/ubiquant/��ͬ��ȡ/���к�ͬ/���Ž�Ͷ/�����Ż���Ʊ�������8��˽ļ֤ȯͶ�ʻ���-�����ͬ-��¶ǿ-20200622173057.docx')
# full_text = contract.get_full_text()

# # print(contract.get_chapter('�����Ͷ��'))
# print(contract.get_section_of_chapter('�����Ͷ��', 'Ͷ�ʷ�Χ'))
# # print(regex.search(r'(?<=--(\t|      )ʮһ�� ˽ļ�����Ͷ��)[\S\s\n\t]{10,}?(?=--(\t|      )ʮ���� ˽ļ����ĲƲ�)', full_text))

contracts = Contracts('/Users/andy/Desktop/work/ubiquant/��ͬ��ȡ/���к�ͬ')
contents = contracts.get_sections('�����Ͷ��', ['Ͷ������', 'Ͷ�ʷ�Χ'])
contracts.to_excel(contracts.get_df(contents), '~/Desktop/output.xlsx')