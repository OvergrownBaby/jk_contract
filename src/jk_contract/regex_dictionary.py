# -*- coding: GBK -*-

from re import S

# regex_chapter_12 = {'中信': '十二、私募基金的投资.+(?<!二)(?=十三)','海通':'基金的投资投资[\S\s\t\n]+(?=基金的财产)','平安':'十一、基金的投资.+(?<!二)(?=十二)',\
#         '光大':'基金的投资投资目标.+基金的财产','招商':'十一、基金的投资.+(?<!二)(?=十二、)','申万':'十二、基金的投资.+(?<!二)(?=十三、)',\
#         '国信':'第七节 基金的投资.+(?=第八节)','国君':'(?<=。)十一、私募基金的投资.+(?<!二)(?=十二)','华泰':'十一、私募基金的投资[\S\s\n]+(?<!二)(?=十二)','广发':'十一、 基金的投资.+(?<!二)(?=十二)'}

def get_chapter_regex(tg, beg_chapter_name, end_chapter_name):
        if tg=='华泰' or tg=='国君' or tg=='招商' or tg=='中信' or tg=='国信' or tg=='平安' or tg=='申万' or tg=='广发': #done
                return r'(?<='+beg_chapter_name+r'[\S\s\n\t]+)'+beg_chapter_name+r'[\S\s\n\t]{10,}?(?='+end_chapter_name+')'
        if tg=='光大': #done
                return r'(?<=--	'+beg_chapter_name+')'+r'[\S\s\n\t]{10,}?(?=--	'+end_chapter_name+')'
        if tg=='海通': #done
                return r'(?<=--	'+beg_chapter_name+'--)'+r'[\S\s\n\t]{10,}?(?=--	'+end_chapter_name+')'

def get_section_regex(tg, beg_section_name, end_section_name):
        if tg=='华泰' or tg=='国信' or tg=='中信' or tg=='平安' or tg=='申万': #done
                return r'(?<='+beg_section_name+r')[\S\s\t\n]+?。(?=[\S\s\t\n]{,5}'+end_section_name+')'
        if tg=='招商': #done
                return r'(?<=（[\S]{1,2}）'+beg_section_name+r')[\S\s\t\n]+?(?=（[\S]{1,2}）'+end_section_name+')'
        if tg=='国君' or tg=='光大': #done
                return r'(?<=--	'+beg_section_name+r')[\S\s\n\t]+?(?=--	'+end_section_name+')'
        if tg=='海通': #done
                return r'(?<=--		'+beg_section_name+r')[\S\s\n\t]+?(?=--		'+end_section_name+')'

def get_section_beg_end(tg, req_section):
        sections_dict = {'华泰':['投资目标','投资范围','投资策略','业绩比较基准','投资限制','投资禁止行为'],
                         '招商':['投资目标','投资范围','投资策略','投资方式','投资比例和投资限制','投资禁止行为','关联交易'],
                         '国君':['投资目标','投资范围','投资限制','关联交易决策以及披露机制','全体基金份额持有人在此授权并同意','预警止损机制','私募基金管理人自有风控措施','基金备案前的现金管理','参与融资融券','投资经理'],
                         '光大':['投资目标','投资范围','投资策略','投资限制','投资经理的指定及变更','业绩比较基准','风险控制','关于穿透原则的特殊约定','投资禁止行为','管理人行使基金财产投资于证券所产生的权利的原则及方法','关联交易','其他'],
                         '国信':['投资目标','投资范围','投资策略','投资限制','投资禁止行为','投资经理的指定和变更','风险控制','关联交易及利益冲突','其他'],
                         '中信':['投资经理','投资目标','投资范围','投资策略','投资限制','投资禁止行为','关联交易及利益冲突的情形及处理方式','风险收益特征','预警止损机制','业绩比较基准','基金托管人投资监督事项的约定'],
                         '广发':['基金财产的保管与处分','基金财产相关账户的开立和管理', '投资范围','投资策略','投资限制','投资禁止行为','关联交易及利益冲突的情形及处理方式','风险收益特征','预警止损机制','业绩比较基准','基金托管人投资监督事项的约定'],
                         '海通':['投资经理','投资目标','投资范围','投资策略','投资限制','投资禁止行为','关联交易的情形及处理方式','风险收益特征','业绩比较基准','参与融资融券业务及其他场外证券业务的情况','预警线与止损线'],
                         '平安':['投资目标','投资范围','投资策略','投资限制','建仓期/封闭期','投资禁止行为','预警止损风险控制设置','业绩比较基准（如有）','风险收益特征','投资政策的变更'],
                         '申万':['投资目标','投资范围','投资策略','投资限制','投资禁止行为','业绩比较基准（如有）','关联交易、可能存在的利益冲突情形及处理方式','参与融资融券及其他场外投资业务的情况（如有）','预警/止损机制','投资经理','投资政策的变更','其他（如有）']}
        return [(section, sections_dict[tg][idx+1]) for idx, section in zip(range(len(sections_dict[tg])), sections_dict[tg]) if req_section in section]

def get_chapter_beg_end(tg, req_chapter):
        chapters_dict = {'华泰':['一、前  言',\
                                '二、释  义',\
                                '三、声明与承诺',\
                                '四、私募基金的基本情况',\
                                '五、私募基金的募集',\
                                '六、私募基金的成立和备案',\
                                '七、私募基金的申购、赎回与转让',\
                                '八、当事人及权利义务',\
                                '九、基金份额持有人大会及日常机构',\
                                '十、私募基金份额的注册登记',\
                                '十一、私募基金的投资',\
                                '十二、私募基金的财产',\
                                '十三、交易及清算交收安排',\
                                '十四、私募基金财产的估值和会计核算',\
                                '十五、私募基金的费用与税收',\
                                '十六、私募基金的收益分配',\
                                '十七、信息披露与报告',\
                                '十八、风险揭示',\
                                '十九、基金合同的效力、变更、解除与终止',\
                                '二十、私募基金的清算',\
                                '二十一、违约责任',\
                                '二十二、争议处理',\
                                '二十三、其他事项'],

                        '招商':['一、前言',\
                                '二、释义',\
                                '三、声明与承诺',\
                                '四、基金的基本情况',\
                                '五、基金的募集',\
                                '六、基金的成立与备案',\
                                '七、基金的申购、赎回、转让和转换',\
                                '八、当事人及权利义务',\
                                '九、基金份额持有人大会及日常机构',\
                                '十、基金份额的登记',\
                                '十一、基金的投资',\
                                '十二、基金的财产',\
                                '十三、指令的发送、确认与执行',\
                                '十四、交易及清算交收安排',\
                                '十五、越权交易',\
                                '十六、基金财产的估值和会计核算',\
                                '十七、基金的费用与税收',\
                                '十八、基金的收益分配',\
                                '十九、基金的信息披露与报告',\
                                '二十、风险揭示',\
                                '二十一、基金份额的非交易过户和冻结、解冻及质押',\
                                '二十二、基金合同的成立、生效及签署',\
                                '二十三、基金合同的效力',\
                                '二十四、基金合同的变更、解除与终止',\
                                '二十五、基金的清算',\
                                '二十六、违约责任',\
                                '二十七、通知与送达',\
                                '二十八、法律适用和争议的处理',\
                                '二十九、侧袋机制',\
                                '三十、其他事项'],

                        '国君':['重要提示',\
                                '一、前言',\
                                '二、释义',\
                                '三、声明与承诺',\
                                '四、私募基金的基本情况',\
                                '五、私募基金的募集',\
                                '六、私募基金的成立与备案',\
                                '七、私募基金的申购、赎回和转让',\
                                '八、当事人及权利义务',\
                                '九、私募基金份额持有人大会及日常机构',\
                                '十、私募基金份额的登记',\
                                '十一、私募基金的投资',\
                                '十二、私募基金的财产',\
                                '十三、交易及清算交收安排',\
                                '十四、越权交易处理',\
                                '十五、私募基金财产的估值和会计核算',\
                                '十六、私募基金的费用与税收',\
                                '十七、私募基金的收益分配',\
                                '十八、信息披露与报告',\
                                '十九、风险揭示',\
                                '二十、基金有关文件档案的保存',\
                                '二十一、基金合同的效力、变更、解除及终止',\
                                '二十二、私募基金的清算',\
                                '二十三、违约责任',\
                                '二十四、法律适用和争议的处理',\
                                '二十五、其他事项',\
                                '附件一：投资监督事项表',\
                                '附件二：私募基金管理人与私募基金管理人委托的基金代理销售机构权利义务（如有）',\
                                '附件三：投资人信息表'],
                                
                        '光大':['前言',\
                                '释义',\
                                '声明与承诺',\
                                '基金的基本情况',\
                                '基金的募集',\
                                '基金的成立和备案',\
                                '基金的申购、赎回与转让',\
                                '当事人及权利义务',\
                                '份额持有人大会及日常机构',\
                                '基金份额的登记',\
                                '基金的投资',\
                                '基金的财产',\
                                '划款指令的发送、确认与执行',\
                                '交易及清算交收安排',\
                                '越权交易',\
                                '基金财产的估值和会计核算',\
                                '基金的费用与税收',\
                                '基金的收益分配',\
                                '信息披露与报告',\
                                '风险揭示',\
                                '基金份额的非交易过户和冻结',\
                                '基金合同的签署、成立及生效',\
                                '基金合同的变更、终止与解除',\
                                '基金的清算',\
                                '违约责任、纠纷解决及维持运作机制',\
                                '通知和送达',\
                                '其他事项',\
                                '投资者及交易信息填写页',\
                                '附件一：投资监督事项表'],
                        
                        '国信':['第一节 前言',\
                                '第二节 释义',\
                                '第三节 声明与承诺',\
                                '第四节 基金的基本情况',\
                                '第五节 基金份额的初始销售',\
                                '第六节 基金的成立与备案',\
                                '第七节 基金的投资',\
                                '第八节 基金份额的申购、赎回',\
                                '第九节 投资冷静期及回访确认',\
                                '第十节 当事人及权利义务',\
                                '第十一节 基金份额持有人大会',\
                                '第十二节 基金份额的登记、转让和非交易过户',\
                                '第十三节 基金的财产',\
                                '第十四节 划款指令的发送、确认与执行',\
                                '第十五节 交易及清算交收安排',\
                                '第十六节 托管人的监督职责',\
                                '第十七节 基金财产的估值和会计核算',\
                                '第十八节 基金的费用与税收',\
                                '第十九节 基金的收益分配',\
                                '第二十节 信息披露与报告',\
                                '第二十一节 风险揭示',\
                                '第二十二节 基金合同的期限、变更、终止',\
                                '第二十三节 基金财产的清算',\
                                '第二十四节 违约责任',\
                                '第二十五节 争议的处理',\
                                '第二十六节 其他事项'],

                        '中信':['重要提示',\
                                '九坤信淮股票多空配置A期私募证券投资基金风险揭示书',\
                                '合格投资者承诺书',\
                                '投资者告知书',\
                                '一、前言',\
                                '二、释义',\
                                '三、声明与承诺',\
                                '四、私募基金的基本情况',\
                                '五、私募基金的结构化安排',\
                                '六、私募基金的募集',\
                                '七、私募基金的成立与备案',\
                                '八、私募基金的申购、赎回和转让',\
                                '九、当事人的权利和义务',\
                                '十、基金份额持有人大会及日常机构',\
                                '十一、私募基金份额的登记',\
                                '十二、私募基金的投资',\
                                '十三、私募基金的财产',\
                                '十四、资金清算交收安排',\
                                '十五、投资指令的发送、确认和执行',\
                                '十六、私募基金资产的估值和会计核算',\
                                '十七、私募基金的费用与税收',\
                                '十八、私募基金的收益分配',\
                                '十九、信息披露与报告',\
                                '二十、风险揭示',\
                                '二十一、私募基金合同的效力、变更、解除与终止',\
                                '二十二、私募基金的清算',\
                                '二十三、违约责任',\
                                '二十四、争议的处理',\
                                '二十五、基金维持运作机制',\
                                '二十六、其他事项'],
                                
                        '广发':['一、 前言',\
                                '二、 释义',\
                                '三、 声明与承诺',\
                                '四、 基金的基本情况',\
                                '五、 基金份额的募集',\
                                '六、 基金的成立与备案',\
                                '七、 基金的申购、赎回和转让',\
                                '八、 当事人及其权利义务',\
                                '九、 基金份额持有人大会及日常机构',\
                                '十、 基金份额的登记',\
                                '十一、 基金的投资',\
                                '十二、 基金的财产',\
                                '十三、 指令的发送、确认与执行',\
                                '十四、 交易及清算交收安排',\
                                '十五、 越权交易',\
                                '十六、 基金财产的估值和会计核算',\
                                '十七、 基金的费用与税收',\
                                '十八、 基金的收益分配',\
                                '十九、 信息披露与报告',\
                                '二十、 风险揭示',\
                                '二十一、 基金份额的非交易过户和冻结、解冻',\
                                '二十二、 基金合同的效力、变更、解除与终止',\
                                '二十三、 基金的清算',\
                                '二十四、 违约责任',\
                                '二十五、 法律适用和争议的处理',\
                                '二十六、 其他事项'],
                        '海通':['重要提示',\
                                '风险揭示书',\
                                '合格投资者承诺书',\
                                '投资者告知书',\
                                '前言',\
                                '释义',\
                                '声明与承诺',\
                                '基金的基本情况',\
                                '基金份额的募集',\
                                '基金的成立与备案',\
                                '基金的申购、赎回和转让',\
                                '当事人及其权利义务',\
                                '基金份额持有人大会及日常机构',\
                                '基金份额的登记',\
                                '基金的投资',\
                                '基金的财产',\
                                '指令的发送、确认与执行',\
                                '十四、 交易及清算交收安排',\
                                '十五、 越权交易',\
                                '十六、 基金财产的估值和会计核算',\
                                '十七、 基金的费用与税收',\
                                '十八、 基金的收益分配',\
                                '十九、 信息披露与报告',\
                                '二十、 基金份额的非交易过户和冻结、解冻',\
                                '二十一、 基金合同的成立、生效',\
                                '二十二、 基金合同的效力、变更、解除与终止',\
                                '二十三、 基金的清算',\
                                '二十四、 违约责任',\
                                '二十五、 法律适用和争议的处理',\
                                '二十六、 其他事项'],

                        '平安':['一、前言',\
                                '二、释义',\
                                '三、声明与承诺',\
                                '四、基金的基本情况',\
                                '五、私募基金的募集',\
                                '六、私募基金的成立与备案',\
                                '七、基金的申购、赎回与转让',\
                                '八、当事人及权利义务',\
                                '九、基金份额持有人大会及日常机构',\
                                '十、基金份额的登记',\
                                '十一、基金的投资',\
                                '十二、投资经理的指定与变更',\
                                '十三、基金的财产',\
                                '十四、划款指令的发送、确认与执行',\
                                '十五、交易及清算交收安排',\
                                '十六、越权交易',\
                                '十七、基金财产的估值和会计核算',\
                                '十八、基金的费用与税收',\
                                '十九、基金的收益分配',\
                                '二十、信息披露与报告',\
                                '二十一、风险揭示',\
                                '二十二、基金合同的效力、解除、变更、终止',\
                                '二十三、清算程序',\
                                '二十四、违约责任',\
                                '二十五、反虚假宣传',\
                                '二十六、反洗钱、反恐怖融资和反逃税条款',\
                                '二十七、法律适用和争议的处理',\
                                '二十八、通知和送达',\
                                '二十九、其他事项'],

                        '申万':['重要提示',\
                                '风险揭示书',\
                                '合格投资者承诺书',\
                                '投资者告知书',\
                                '目录',\
                                '一、前言',\
                                '二、释义',\
                                '三、声明与承诺',\
                                '四、基金的基本情况',\
                                '五、基金的募集',\
                                '六、基金的成立与备案',\
                                '七、基金的申购和赎回',\
                                '八、当事人及权利义务',\
                                '九、基金份额持有人大会',\
                                '十、基金份额的登记',\
                                '十一、基金份额的转让、非交易过户和冻结、解冻',\
                                '十二、基金的投资',\
                                '十三、基金的财产',\
                                '十四、交易及清算交收安排',\
                                '十五、指令的发送、确认与执行',\
                                '十六、越权交易处理',\
                                '十七、基金财产的估值和净值计算',\
                                '十八、基金的费用与税收',\
                                '十九、基金的收益分配',\
                                '二十、信息披露',\
                                '二十一、基金有关文件档案的保存',\
                                '二十二、私募基金托管人和私募基金管理人的更换',\
                                '二十三、风险揭示',\
                                '二十四、基金合同的效力、变更、解除和终止',\
                                '二十五、清算程序',\
                                '二十六、违约责任',\
                                '二十七、法律适用和争议的处理',\
                                '二十八、通知和送达',\
                                '二十九、其他事项']}

        return [(chapter, chapters_dict[tg][idx+1]) for idx, chapter in zip(range(len(chapters_dict[tg])), chapters_dict[tg]) if req_chapter in chapter]