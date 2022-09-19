# -*- coding: GBK -*-

import regex
from jk_contract import Contract
from jk_contract import Contracts

# contract = Contract('/Users/andy/Desktop/work/ubiquant/合同提取/所有合同/中信建投/九坤信淮股票多空配置8号私募证券投资基金-基金合同-苗露强-20200622173057.docx')
# full_text = contract.get_full_text()

# # print(contract.get_chapter('基金的投资'))
# print(contract.get_section_of_chapter('基金的投资', '投资范围'))
# # print(regex.search(r'(?<=--(\t|      )十一、 私募基金的投资)[\S\s\n\t]{10,}?(?=--(\t|      )十二、 私募基金的财产)', full_text))

contracts = Contracts('/Users/andy/Desktop/work/ubiquant/合同提取/所有合同')
contents = contracts.get_sections('基金的投资', ['投资限制', '投资范围'])
contracts.to_excel(contracts.get_df(contents), '~/Desktop/output.xlsx')