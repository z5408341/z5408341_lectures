""" week10_slides_main.py

This module includes the data we will use in the simplified version of the
event study discussed in class

IMPORTANT: The simplified version of the event study includes the following
files

    toolkit/
    |   ...
    |__ webinars/
    |   |__ week10/
    |   |   |__ __init__.py
    |   |   |__ week10_slides_main.py
    |   |   |__ week10_slides_data.py       <- this module
    |   |__ lec_utils.py            <- Required

"""

from webinars import lec_utils as utils


cnts_prc_csv = """
date       , open   , high   , low    , close  , adj_close
2020-09-18 , 447.94 , 451    , 428.8  , 442.15 , 442.15
2020-09-21 , 453.13 , 455.68 , 407.07 , 449.39 , 449.39
2020-09-22 , 429.6  , 437.76 , 417.6  , 424.23 , 424.23
2020-09-23 , 405.16 , 412.15 , 375.88 , 380.36 , 380.36
2020-09-24 , 363.8  , 399.5  , 351.3  , 387.79 , 387.79
2020-09-25 , 393.47 , 408.73 , 391.3  , 407.34 , 407.34
"""


cnts_rec_csv = """
date                , firm           , to_grade    , from_grade   , action
2012-02-16 07:42:00 , JP Morgan      , Overweight  ,              , main
2020-09-23 08:58:55 , Deutsche Bank  , Hold        ,              , main
2020-09-23 09:01:26 , Deutsche Bank  , Hold        ,              , main
2020-09-23 09:11:01 , Wunderlich     , Sell        , Buy          , down
2020-09-23 11:15:12 , Deutsche bank  , Buy         , Hold         , up
2020-11-18 11:07:44 , Morgan Stanley , Overweight  , Equal-Weight , up
2020-12-09 15:34:34 , JP Morgan      , Underweight ,              , main
"""

cnts_mkt_csv = """
date       , mkt
2020-09-18 , -0.0088
2020-09-21 , -0.0108
2020-09-22 , 0.0102
2020-09-23 , -0.0248
2020-09-24 , 0.0025
2020-09-25 , 0.0172
"""

cnts_cars_csv = """
event_id , firm                , event_date , event_type , car
1        , WUNDERLICH          , 2012-02-16 , downgrade  , 0.098288644
2        , WUNDERLICH          , 2012-03-26 , upgrade    , 0.103184201
3        , MORGAN STANLEY      , 2012-09-17 , upgrade    , 0.028515908
4        , BANK OF AMERICA     , 2013-02-21 , downgrade  , -0.01564567
5        , GOLDMAN SACHS       , 2013-05-09 , downgrade  , 0.275887761
6        , DEUTSCHE BANK       , 2013-07-26 , upgrade    , 0.053379938
7        , BARCLAYS            , 2013-08-08 , downgrade  , 0.076280435
8        , LAZARD              , 2013-08-12 , downgrade  , -0.08850144
9        , BAIRD               , 2013-10-02 , downgrade  , -0.05107563
10       , WEDBUSH             , 2013-10-15 , upgrade    , 0.005182622
11       , STANDPOINT RESEARCH , 2013-11-07 , upgrade    , -0.22455352
12       , S&P CAPITAL IQ      , 2013-11-27 , upgrade    , 0.045359951
13       , BAIRD               , 2014-01-14 , upgrade    , 0.170110778
14       , DEUTSCHE BANK       , 2014-02-20 , downgrade  , 0.059377408
15       , S&P CAPITAL IQ      , 2014-02-20 , downgrade  , 0.059377408
16       , S&P CAPITAL IQ      , 2014-05-07 , upgrade    , -0.13254282
17       , DEUTSCHE BANK       , 2014-08-11 , upgrade    , 0.040311697
18       , STIFEL NICOLAUS     , 2014-09-02 , upgrade    , 0.062902427
19       , JP MORGAN           , 2015-02-12 , downgrade  , -0.08933714
20       , CLSA                , 2015-03-25 , downgrade  , -0.04532215
21       , DEUTSCHE BANK       , 2015-07-07 , downgrade  , -0.06772031
22       , PACIFIC CREST       , 2015-07-08 , downgrade  , -0.07535135
23       , UBS                 , 2015-07-21 , downgrade  , -0.01298572
24       , BAIRD               , 2015-10-07 , downgrade  , -0.14731993
25       , BARCLAYS            , 2015-10-09 , downgrade  , -0.10753076
26       , BAIRD               , 2016-03-14 , upgrade    , 0.066666616
27       , STANDPOINT RESEARCH , 2016-04-07 , downgrade  , 0.021989817
28       , GOLDMAN SACHS       , 2016-05-18 , upgrade    , 0.054796502
29       , OPPENHEIMER         , 2016-06-22 , downgrade  , -0.08780154
30       , MORGAN STANLEY      , 2016-06-23 , downgrade  , -0.10034296
31       , STANDPOINT RESEARCH , 2016-06-24 , upgrade    , -0.09784337
32       , GOLDMAN SACHS       , 2016-10-06 , downgrade  , -0.07905699
33       , MORGAN STANLEY      , 2017-01-19 , upgrade    , 0.032387556
34       , GOLDMAN SACHS       , 2017-02-27 , downgrade  , -0.03916632
35       , PIPERJAFFRAY        , 2017-04-10 , upgrade    , -0.01298278
36       , MORGAN STANLEY      , 2017-05-15 , downgrade  , -0.04350942
37       , ARGUS               , 2017-08-08 , upgrade    , 0.013689714
38       , STANDPOINT RESEARCH , 2017-10-04 , downgrade  , 0.033011650
39       , EVERCORE ISI GROUP  , 2017-10-27 , downgrade  , -0.05430664
40       , STANDPOINT RESEARCH , 2018-03-26 , upgrade    , -0.15440616
41       , JEFFERIES           , 2018-04-02 , upgrade    , 0.079880551
42       , NEEDHAM             , 2018-07-19 , downgrade  , 0.009470235
43       , OPPENHEIMER         , 2018-08-02 , upgrade    , 0.181173463
44       , NOMURA              , 2018-09-11 , downgrade  , 0.088860775
45       , CITIGROUP           , 2018-09-28 , downgrade  , -0.11529042
46       , JEFFERIES           , 2018-12-07 , upgrade    , 0.020721386
47       , RBC CAPITAL         , 2019-01-23 , downgrade  , -0.01345248
48       , CANACCORD GENUITY   , 2019-02-11 , upgrade    , -0.00944462
49       , EVERCORE ISI GROUP  , 2019-04-22 , downgrade  , -0.06214079
50       , WEDBUSH             , 2019-04-25 , downgrade  , -0.11946021
51       , WOLFE RESEARCH      , 2019-05-02 , downgrade  , 0.056144746
52       , ROTH CAPITAL        , 2019-06-10 , upgrade    , 0.022858965
53       , ROTH CAPITAL        , 2019-07-22 , downgrade  , 0.010651396
54       , JMP SECURITIES      , 2019-10-03 , downgrade  , -0.03014387
55       , ROTH CAPITAL        , 2019-10-29 , downgrade  , -0.04397359
56       , BAIRD               , 2020-01-09 , downgrade  , 0.053773023
57       , MORGAN STANLEY      , 2020-01-16 , downgrade  , -0.03906459
58       , NEW STREET          , 2020-02-04 , downgrade  , 0.147595980
59       , CANACCORD GENUITY   , 2020-02-05 , downgrade  , 0.151967606
60       , JEFFERIES           , 2020-02-25 , downgrade  , -0.15732492
61       , JMP SECURITIES      , 2020-03-03 , upgrade    , 0.066351687
62       , B OF A SECURITIES   , 2020-03-18 , upgrade    , -0.05031295
63       , MORGAN STANLEY      , 2020-03-19 , upgrade    , 0.015405082
64       , ARGUS RESEARCH      , 2020-03-24 , downgrade  , 0.086225480
65       , UBS                 , 2020-03-24 , upgrade    , 0.086225480
66       , JEFFERIES           , 2020-04-06 , upgrade    , 0.034774845
67       , CREDIT SUISSE       , 2020-04-14 , upgrade    , 0.270045308
68       , B OF A SECURITIES   , 2020-04-22 , downgrade  , -0.02470541
69       , GOLDMAN SACHS       , 2020-06-12 , downgrade  , 0.051959290
70       , MORGAN STANLEY      , 2020-06-12 , downgrade  , 0.051959290
71       , JMP SECURITIES      , 2020-07-21 , downgrade  , 0.010198612
72       , NEW STREET          , 2020-07-23 , downgrade  , -0.13041518
73       , ARGUS RESEARCH      , 2020-07-24 , upgrade    , -0.08338607
74       , BERNSTEIN           , 2020-07-28 , downgrade  , 0.041798483
75       , B OF A SECURITIES   , 2020-09-23 , upgrade    , -0.06737533
76       , BERNSTEIN           , 2020-09-23 , downgrade  , -0.06737533
77       , CFRA                , 2020-09-23 , downgrade  , -0.06737533
78       , CHINA RENAISSANCE   , 2020-09-23 , downgrade  , -0.06737533
79       , COWEN & CO.         , 2020-09-23 , upgrade    , -0.06737533
80       , DAIWA CAPITAL       , 2020-09-23 , downgrade  , -0.06737533
81       , DEUTSCHE BANK       , 2020-09-23 , upgrade    , -0.06737533
82       , EXANE BNP PARIBAS   , 2020-09-23 , downgrade  , -0.06737533
83       , MORGAN STANLEY      , 2020-09-23 , upgrade    , -0.06737533
84       , ROTH CAPITAL        , 2020-09-23 , upgrade    , -0.06737533
85       , WUNDERLICH          , 2020-09-23 , downgrade  , -0.06737533
86       , NEW STREET          , 2020-10-08 , upgrade    , -0.00261261
87       , BAIRD               , 2020-10-22 , upgrade    , -0.03394104
88       , JMP SECURITIES      , 2020-10-22 , upgrade    , -0.03394104
89       , MORGAN STANLEY      , 2020-11-18 , upgrade    , 0.187908073
90       , GOLDMAN SACHS       , 2020-12-03 , upgrade    , 0.032789198
91       , NEW STREET          , 2020-12-10 , downgrade  , -0.04187319
92       , JEFFERIES           , 2020-12-11 , downgrade  , -0.04982589
93       , CFRA                , 2020-12-18 , downgrade  , 0.087861007
"""

cars_df = utils.csv_to_df(cnts_cars_csv,
        index_col='event_id',
        parse_dates=['event_date'])
