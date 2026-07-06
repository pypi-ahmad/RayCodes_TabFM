## 1. Input Data (Training Context)
```text
       species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0       Adelie      Dream            39.5           16.7              178.0       3250.0  FEMALE
1       Gentoo     Biscoe            46.9           14.6              222.0       4875.0  FEMALE
2       Adelie  Torgersen            42.1           19.1              195.0       4000.0    MALE
3    Chinstrap      Dream            49.8           17.3              198.0       3675.0  FEMALE
4       Adelie     Biscoe            41.1           18.2              192.0       4050.0    MALE
5       Gentoo     Biscoe            44.9           13.8              212.0       4750.0  FEMALE
6       Gentoo     Biscoe            50.7           15.0              223.0       5550.0    MALE
7    Chinstrap      Dream            49.7           18.6              195.0       3600.0    MALE
8    Chinstrap      Dream            49.6           18.2              193.0       3775.0    MALE
9    Chinstrap      Dream            51.4           19.0              201.0       3950.0    MALE
10      Adelie  Torgersen            42.9           17.6              196.0       4700.0    MALE
11      Adelie  Torgersen            34.6           21.1              198.0       4400.0    MALE
12      Gentoo     Biscoe            43.3           14.0              208.0       4575.0  FEMALE
13      Adelie      Dream            36.8           18.5              193.0       3500.0  FEMALE
14      Gentoo     Biscoe            45.1           14.4              210.0       4400.0  FEMALE
15      Adelie      Dream            37.0           16.5              185.0       3400.0  FEMALE
16      Adelie  Torgersen            36.2           17.2              187.0       3150.0  FEMALE
17   Chinstrap      Dream            46.5           17.9              192.0       3500.0  FEMALE
18      Adelie  Torgersen            36.7           18.8              187.0       3800.0  FEMALE
19      Gentoo     Biscoe            45.7           13.9              214.0       4400.0  FEMALE
20      Adelie     Biscoe            42.7           18.3              196.0       4075.0    MALE
21      Adelie      Dream            40.7           17.0              190.0       3725.0    MALE
22      Gentoo     Biscoe            49.1           15.0              228.0       5500.0    MALE
23   Chinstrap      Dream            50.7           19.7              203.0       4050.0    MALE
24      Adelie  Torgersen            38.9           17.8              181.0       3625.0  FEMALE
25      Adelie  Torgersen            38.6           17.0              188.0       2900.0  FEMALE
26      Gentoo     Biscoe            44.9           13.3              213.0       5100.0  FEMALE
27      Gentoo     Biscoe            43.5           15.2              213.0       4650.0  FEMALE
28   Chinstrap      Dream            58.0           17.8              181.0       3700.0  FEMALE
29      Gentoo     Biscoe            49.8           15.9              229.0       5950.0    MALE
30   Chinstrap      Dream            43.2           16.6              187.0       2900.0  FEMALE
31      Gentoo     Biscoe            52.1           17.0              230.0       5550.0    MALE
32      Adelie  Torgersen            41.8           19.4              198.0       4450.0    MALE
33      Adelie      Dream            35.7           18.0              202.0       3550.0  FEMALE
34      Gentoo     Biscoe            49.8           16.8              230.0       5700.0    MALE
35      Gentoo     Biscoe            47.5           14.2              209.0       4600.0  FEMALE
36   Chinstrap      Dream            47.6           18.3              195.0       3850.0  FEMALE
37      Gentoo     Biscoe            42.7           13.7              208.0       3950.0  FEMALE
38      Adelie     Biscoe            35.0           17.9              190.0       3450.0  FEMALE
39      Adelie  Torgersen            35.2           15.9              186.0       3050.0  FEMALE
40      Adelie      Dream            37.6           19.3              181.0       3300.0  FEMALE
41      Adelie      Dream            36.0           17.9              190.0       3450.0  FEMALE
42   Chinstrap      Dream            50.5           18.4              200.0       3400.0  FEMALE
43   Chinstrap      Dream            47.5           16.8              199.0       3900.0  FEMALE
44      Adelie  Torgersen            41.1           18.6              189.0       3325.0    MALE
45      Adelie  Torgersen            36.2           16.1              187.0       3550.0  FEMALE
46      Gentoo     Biscoe            46.2           14.9              221.0       5300.0    MALE
47      Adelie     Biscoe            40.1           18.9              188.0       4300.0    MALE
48      Adelie     Biscoe            38.2           20.0              190.0       3900.0    MALE
49      Gentoo     Biscoe            48.5           15.0              219.0       4850.0  FEMALE
50      Adelie     Biscoe            35.0           17.9              192.0       3725.0  FEMALE
51      Gentoo     Biscoe            49.3           15.7              217.0       5850.0    MALE
52      Gentoo     Biscoe            45.4           14.6              211.0       4800.0  FEMALE
53      Adelie     Biscoe            37.7           18.7              180.0       3600.0    MALE
54      Adelie     Biscoe            39.6           20.7              191.0       3900.0  FEMALE
55      Gentoo     Biscoe            48.4           16.3              220.0       5400.0    MALE
56      Adelie  Torgersen            41.1           17.6              182.0       3200.0  FEMALE
57      Adelie     Biscoe            41.3           21.1              195.0       4400.0    MALE
58   Chinstrap      Dream            50.0           19.5              196.0       3900.0    MALE
59   Chinstrap      Dream            51.0           18.8              203.0       4100.0    MALE
60      Gentoo     Biscoe            50.8           17.3              228.0       5600.0    MALE
61      Gentoo     Biscoe            46.8           16.1              215.0       5500.0    MALE
62      Gentoo     Biscoe            43.5           14.2              220.0       4700.0  FEMALE
63      Adelie  Torgersen            36.7           19.3              193.0       3450.0  FEMALE
64      Adelie  Torgersen            35.1           19.4              193.0       4200.0    MALE
65      Gentoo     Biscoe            51.1           16.5              225.0       5250.0    MALE
66      Adelie     Biscoe            35.5           16.2              195.0       3350.0  FEMALE
67      Gentoo     Biscoe            40.9           13.7              214.0       4650.0  FEMALE
68      Adelie      Dream            37.3           17.8              191.0       3350.0  FEMALE
69      Gentoo     Biscoe            50.0           15.9              224.0       5350.0    MALE
70      Adelie     Biscoe            35.9           19.2              189.0       3800.0  FEMALE
71      Adelie     Biscoe            40.5           18.9              180.0       3950.0    MALE
72      Gentoo     Biscoe            44.4           17.3              219.0       5250.0    MALE
73      Gentoo     Biscoe            46.2           14.1              217.0       4375.0  FEMALE
74      Gentoo     Biscoe            42.9           13.1              215.0       5000.0  FEMALE
75   Chinstrap      Dream            54.2           20.8              201.0       4300.0    MALE
76      Adelie      Dream            38.3           19.2              189.0       3950.0    MALE
77      Adelie  Torgersen            37.3           20.5              199.0       3775.0    MALE
78      Adelie      Dream            37.8           18.1              193.0       3750.0    MALE
79      Gentoo     Biscoe            47.8           15.0              215.0       5650.0    MALE
80      Adelie  Torgersen            40.2           17.0              176.0       3450.0  FEMALE
81      Adelie      Dream            39.2           18.6              190.0       4250.0    MALE
82   Chinstrap      Dream            40.9           16.6              187.0       3200.0  FEMALE
83      Adelie      Dream            38.1           18.6              190.0       3700.0  FEMALE
84      Gentoo     Biscoe            55.9           17.0              228.0       5600.0    MALE
85      Gentoo     Biscoe            43.6           13.9              217.0       4900.0  FEMALE
86      Adelie      Dream            38.8           20.0              190.0       3950.0    MALE
87      Gentoo     Biscoe            47.5           14.0              212.0       4875.0  FEMALE
88   Chinstrap      Dream            53.5           19.9              205.0       4500.0    MALE
89   Chinstrap      Dream            48.5           17.5              191.0       3400.0    MALE
90      Gentoo     Biscoe            50.2           14.3              218.0       5700.0    MALE
91      Gentoo     Biscoe            50.4           15.7              222.0       5750.0    MALE
92      Adelie      Dream            41.5           18.5              201.0       4000.0    MALE
93      Adelie     Biscoe            41.6           18.0              192.0       3950.0    MALE
94      Adelie  Torgersen            40.6           19.0              199.0       4000.0    MALE
95      Adelie     Biscoe            37.8           18.3              174.0       3400.0  FEMALE
96      Adelie  Torgersen            39.2           19.6              195.0       4675.0    MALE
97   Chinstrap      Dream            55.8           19.8              207.0       4000.0    MALE
98      Adelie      Dream            43.2           18.5              192.0       4100.0    MALE
99      Adelie      Dream            39.2           21.1              196.0       4150.0    MALE
100     Adelie     Biscoe            40.5           17.9              187.0       3200.0  FEMALE
101     Gentoo     Biscoe            48.2           15.6              221.0       5100.0    MALE
102     Gentoo     Biscoe            47.4           14.6              212.0       4725.0  FEMALE
103     Adelie     Biscoe            37.6           17.0              185.0       3600.0  FEMALE
104  Chinstrap      Dream            52.8           20.0              205.0       4550.0    MALE
105     Adelie  Torgersen            36.6           17.8              185.0       3700.0  FEMALE
106     Gentoo     Biscoe            49.0           16.1              216.0       5550.0    MALE
107     Gentoo     Biscoe            48.4           14.6              213.0       5850.0    MALE
108     Adelie      Dream            36.9           18.6              189.0       3500.0  FEMALE
109  Chinstrap      Dream            51.3           18.2              197.0       3750.0    MALE
110     Adelie      Dream            37.0           16.9              185.0       3000.0  FEMALE
111     Gentoo     Biscoe            48.4           14.4              203.0       4625.0  FEMALE
112     Adelie     Biscoe            38.1           16.5              198.0       3825.0  FEMALE
113  Chinstrap      Dream            51.3           19.9              198.0       3700.0    MALE
114  Chinstrap      Dream            49.0           19.6              212.0       4300.0    MALE
115  Chinstrap      Dream            47.0           17.3              185.0       3700.0  FEMALE
116     Adelie  Torgersen            38.5           17.9              190.0       3325.0  FEMALE
117     Gentoo     Biscoe            45.8           14.6              210.0       4200.0  FEMALE
118     Adelie  Torgersen            39.6           17.2              196.0       3550.0  FEMALE
119  Chinstrap      Dream            43.5           18.1              202.0       3400.0  FEMALE
120     Adelie     Biscoe            38.2           18.1              185.0       3950.0    MALE
121  Chinstrap      Dream            48.1           16.4              199.0       3325.0  FEMALE
122     Gentoo     Biscoe            46.5           14.4              217.0       4900.0  FEMALE
123     Adelie      Dream            39.0           18.7              185.0       3650.0    MALE
124     Adelie     Biscoe            38.8           17.2              180.0       3800.0    MALE
125     Gentoo     Biscoe            47.2           13.7              214.0       4925.0  FEMALE
126     Adelie      Dream            33.1           16.1              178.0       2900.0  FEMALE
127     Adelie      Dream            41.3           20.3              194.0       3550.0    MALE
128     Adelie  Torgersen            42.8           18.5              195.0       4250.0    MALE
129  Chinstrap      Dream            45.7           17.0              195.0       3650.0  FEMALE
130     Adelie     Biscoe            37.7           16.0              183.0       3075.0  FEMALE
131     Adelie     Biscoe            37.8           20.0              190.0       4250.0    MALE
132  Chinstrap      Dream            45.7           17.3              193.0       3600.0  FEMALE
133     Adelie  Torgersen            35.5           17.5              190.0       3700.0  FEMALE
134     Adelie     Biscoe            37.9           18.6              172.0       3150.0  FEMALE
135     Adelie      Dream            36.0           18.5              186.0       3100.0  FEMALE
136     Gentoo     Biscoe            59.6           17.0              230.0       6050.0    MALE
137     Adelie  Torgersen            45.8           18.9              197.0       4150.0    MALE
138     Gentoo     Biscoe            50.1           15.0              225.0       5000.0    MALE
139     Adelie      Dream            36.0           17.1              187.0       3700.0  FEMALE
140     Adelie  Torgersen            43.1           19.2              197.0       3500.0    MALE
141     Gentoo     Biscoe            46.7           15.3              219.0       5200.0    MALE
142     Adelie      Dream            34.0           17.1              185.0       3400.0  FEMALE
143     Gentoo     Biscoe            47.7           15.0              216.0       4750.0  FEMALE
144  Chinstrap      Dream            46.1           18.2              178.0       3250.0  FEMALE
145     Gentoo     Biscoe            46.4           15.6              221.0       5000.0    MALE
146  Chinstrap      Dream            51.3           19.2              193.0       3650.0    MALE
147     Gentoo     Biscoe            45.2           16.4              223.0       5950.0    MALE
148     Gentoo     Biscoe            46.1           15.1              215.0       5100.0    MALE
149     Gentoo     Biscoe            43.3           13.4              209.0       4400.0  FEMALE
150  Chinstrap      Dream            51.7           20.3              194.0       3775.0    MALE
151     Gentoo     Biscoe            46.5           13.5              210.0       4550.0  FEMALE
152     Adelie      Dream            41.1           17.5              190.0       3900.0    MALE
153     Adelie      Dream            44.1           19.7              196.0       4400.0    MALE
154     Gentoo     Biscoe            46.3           15.8              215.0       5050.0    MALE
155  Chinstrap      Dream            49.3           19.9              203.0       4050.0    MALE
156  Chinstrap      Dream            49.2           18.2              195.0       4400.0    MALE
157     Adelie  Torgersen            35.7           17.0              189.0       3350.0  FEMALE
158  Chinstrap      Dream            45.2           16.6              191.0       3250.0  FEMALE
159  Chinstrap      Dream            51.5           18.7              187.0       3250.0    MALE
160     Adelie  Torgersen            41.4           18.5              202.0       3875.0    MALE
161     Gentoo     Biscoe            53.4           15.8              219.0       5500.0    MALE
162     Gentoo     Biscoe            50.5           15.2              216.0       5000.0  FEMALE
163     Gentoo     Biscoe            47.5           15.0              218.0       4950.0  FEMALE
164  Chinstrap      Dream            46.4           18.6              190.0       3450.0  FEMALE
165     Gentoo     Biscoe            46.8           15.4              215.0       5150.0    MALE
166     Gentoo     Biscoe            45.5           13.7              214.0       4650.0  FEMALE
167  Chinstrap      Dream            46.0           18.9              195.0       4150.0  FEMALE
168     Gentoo     Biscoe            49.2           15.2              221.0       6300.0    MALE
169     Adelie  Torgersen            40.3           18.0              195.0       3250.0  FEMALE
170     Adelie  Torgersen            37.7           19.8              198.0       3500.0    MALE
171  Chinstrap      Dream            49.5           19.0              200.0       3800.0    MALE
172     Gentoo     Biscoe            50.4           15.3              224.0       5550.0    MALE
173     Adelie  Torgersen            38.8           17.6              191.0       3275.0  FEMALE
174     Gentoo     Biscoe            41.7           14.7              210.0       4700.0  FEMALE
175     Gentoo     Biscoe            51.1           16.3              220.0       6000.0    MALE
176     Adelie      Dream            37.5           18.5              199.0       4475.0    MALE
177     Adelie  Torgersen            34.6           17.2              189.0       3200.0  FEMALE
178     Adelie      Dream            36.4           17.0              195.0       3325.0  FEMALE
179     Adelie      Dream            38.9           18.8              190.0       3600.0  FEMALE
180     Gentoo     Biscoe            45.8           14.2              219.0       4700.0  FEMALE
181     Adelie     Biscoe            42.2           19.5              197.0       4275.0    MALE
182  Chinstrap      Dream            52.0           20.7              210.0       4800.0    MALE
183     Gentoo     Biscoe            49.5           16.2              229.0       5800.0    MALE
184     Adelie      Dream            39.7           17.9              193.0       4250.0    MALE
185  Chinstrap      Dream            46.9           16.6              192.0       2700.0  FEMALE
186     Gentoo     Biscoe            46.2           14.5              209.0       4800.0  FEMALE
187     Adelie     Biscoe            39.6           17.7              186.0       3500.0  FEMALE
188     Gentoo     Biscoe            50.8           15.7              226.0       5200.0    MALE
189     Adelie  Torgersen            39.7           18.4              190.0       3900.0    MALE
190     Gentoo     Biscoe            49.1           14.5              212.0       4625.0  FEMALE
191     Adelie      Dream            41.1           18.1              205.0       4300.0    MALE
192  Chinstrap      Dream            49.0           19.5              210.0       3950.0    MALE
193     Adelie  Torgersen            40.9           16.8              191.0       3700.0  FEMALE
194  Chinstrap      Dream            52.0           18.1              201.0       4050.0    MALE
195     Adelie  Torgersen            42.5           20.7              197.0       4500.0    MALE
196     Adelie      Dream            36.5           18.0              182.0       3150.0  FEMALE
197     Adelie      Dream            40.9           18.9              184.0       3900.0    MALE
198  Chinstrap      Dream            46.7           17.9              195.0       3300.0  FEMALE
199     Adelie      Dream            36.0           17.8              195.0       3450.0  FEMALE
```

## 2. Target Data (To Predict)
```text
       island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0      Biscoe            45.2           13.8              215.0       4750.0  FEMALE
1      Biscoe            46.5           14.5              213.0       4400.0  FEMALE
2       Dream            46.8           16.5              189.0       3650.0  FEMALE
3       Dream            50.8           19.0              210.0       4100.0    MALE
4      Biscoe            45.5           14.5              212.0       4750.0  FEMALE
5      Biscoe            44.0           13.6              208.0       4350.0  FEMALE
6      Biscoe            51.5           16.3              230.0       5500.0    MALE
7      Biscoe            49.5           16.1              224.0       5650.0    MALE
8      Biscoe            43.8           13.9              208.0       4300.0  FEMALE
9       Dream            52.2           18.8              197.0       3450.0    MALE
10      Dream            50.5           19.6              201.0       4050.0    MALE
11      Dream            42.3           21.2              191.0       4150.0    MALE
12     Biscoe            50.0           15.2              218.0       5700.0    MALE
13      Dream            50.9           17.9              196.0       3675.0  FEMALE
14     Biscoe            45.5           13.9              210.0       4200.0  FEMALE
15     Biscoe            45.6           20.3              191.0       4600.0    MALE
16     Biscoe            37.6           19.1              194.0       3750.0    MALE
17  Torgersen            39.5           17.4              186.0       3800.0  FEMALE
18     Biscoe            41.4           18.6              191.0       3700.0    MALE
19      Dream            36.3           19.5              190.0       3800.0    MALE
20      Dream            45.6           19.4              194.0       3525.0  FEMALE
21      Dream            39.8           19.1              184.0       4650.0    MALE
22     Biscoe            46.6           14.2              210.0       4850.0  FEMALE
23      Dream            40.3           18.5              196.0       4350.0    MALE
24     Biscoe            36.5           16.6              181.0       2850.0  FEMALE
25     Biscoe            48.5           14.1              220.0       5300.0    MALE
26     Biscoe            48.2           14.3              210.0       4600.0  FEMALE
27  Torgersen            34.4           18.4              184.0       3325.0  FEMALE
28      Dream            36.2           17.3              187.0       3300.0  FEMALE
29     Biscoe            45.3           13.8              208.0       4200.0  FEMALE
30      Dream            42.4           17.3              181.0       3600.0  FEMALE
31     Biscoe            48.8           16.2              222.0       6000.0    MALE
32      Dream            40.2           17.1              193.0       3400.0  FEMALE
33     Biscoe            48.1           15.1              209.0       5500.0    MALE
34     Biscoe            47.3           15.3              222.0       5250.0    MALE
35     Biscoe            35.7           16.9              185.0       3150.0  FEMALE
36     Biscoe            39.0           17.5              186.0       3550.0  FEMALE
37      Dream            46.4           17.8              191.0       3700.0  FEMALE
38      Dream            45.5           17.0              196.0       3500.0  FEMALE
39     Biscoe            45.2           14.8              212.0       5200.0  FEMALE
40      Dream            46.2           17.5              187.0       3650.0  FEMALE
41      Dream            50.6           19.4              193.0       3800.0    MALE
42     Biscoe            36.4           17.1              184.0       2850.0  FEMALE
43     Biscoe            34.5           18.1              187.0       2900.0  FEMALE
44     Biscoe            45.1           14.5              215.0       5000.0  FEMALE
45     Biscoe            48.7           15.7              208.0       5350.0    MALE
46     Biscoe            40.6           18.6              183.0       3550.0    MALE
47      Dream            45.9           17.1              190.0       3575.0  FEMALE
48     Biscoe            54.3           15.7              231.0       5650.0    MALE
49      Dream            50.8           18.5              201.0       4450.0    MALE
50     Biscoe            52.5           15.6              221.0       5450.0    MALE
51     Biscoe            50.5           15.9              222.0       5550.0    MALE
52     Biscoe            49.4           15.8              216.0       4925.0    MALE
53      Dream            45.4           18.7              188.0       3525.0  FEMALE
54      Dream            35.6           17.5              191.0       3175.0  FEMALE
55      Dream            45.2           17.8              198.0       3950.0  FEMALE
56     Biscoe            39.7           18.9              184.0       3550.0    MALE
57      Dream            39.6           18.1              186.0       4450.0    MALE
58     Biscoe            46.1           13.2              211.0       4500.0  FEMALE
59  Torgersen            41.5           18.3              195.0       4300.0    MALE
60     Biscoe            49.9           16.1              213.0       5400.0    MALE
61     Biscoe            35.3           18.9              187.0       3800.0  FEMALE
62      Dream            50.9           19.1              196.0       3550.0    MALE
63  Torgersen            37.2           19.4              184.0       3900.0    MALE
64     Biscoe            39.7           17.7              193.0       3200.0  FEMALE
65     Biscoe            45.5           15.0              220.0       5000.0    MALE
66     Biscoe            38.1           17.0              181.0       3175.0  FEMALE
```

## 3. TabFM Predictions
```text
       island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex Predicted_species
0      Biscoe            45.2           13.8              215.0       4750.0  FEMALE            Gentoo
1      Biscoe            46.5           14.5              213.0       4400.0  FEMALE            Gentoo
2       Dream            46.8           16.5              189.0       3650.0  FEMALE         Chinstrap
3       Dream            50.8           19.0              210.0       4100.0    MALE         Chinstrap
4      Biscoe            45.5           14.5              212.0       4750.0  FEMALE            Gentoo
5      Biscoe            44.0           13.6              208.0       4350.0  FEMALE            Gentoo
6      Biscoe            51.5           16.3              230.0       5500.0    MALE            Gentoo
7      Biscoe            49.5           16.1              224.0       5650.0    MALE            Gentoo
8      Biscoe            43.8           13.9              208.0       4300.0  FEMALE            Gentoo
9       Dream            52.2           18.8              197.0       3450.0    MALE         Chinstrap
10      Dream            50.5           19.6              201.0       4050.0    MALE         Chinstrap
11      Dream            42.3           21.2              191.0       4150.0    MALE            Adelie
12     Biscoe            50.0           15.2              218.0       5700.0    MALE            Gentoo
13      Dream            50.9           17.9              196.0       3675.0  FEMALE         Chinstrap
14     Biscoe            45.5           13.9              210.0       4200.0  FEMALE            Gentoo
15     Biscoe            45.6           20.3              191.0       4600.0    MALE            Adelie
16     Biscoe            37.6           19.1              194.0       3750.0    MALE            Adelie
17  Torgersen            39.5           17.4              186.0       3800.0  FEMALE            Adelie
18     Biscoe            41.4           18.6              191.0       3700.0    MALE            Adelie
19      Dream            36.3           19.5              190.0       3800.0    MALE            Adelie
20      Dream            45.6           19.4              194.0       3525.0  FEMALE         Chinstrap
21      Dream            39.8           19.1              184.0       4650.0    MALE            Adelie
22     Biscoe            46.6           14.2              210.0       4850.0  FEMALE            Gentoo
23      Dream            40.3           18.5              196.0       4350.0    MALE            Adelie
24     Biscoe            36.5           16.6              181.0       2850.0  FEMALE            Adelie
25     Biscoe            48.5           14.1              220.0       5300.0    MALE            Gentoo
26     Biscoe            48.2           14.3              210.0       4600.0  FEMALE            Gentoo
27  Torgersen            34.4           18.4              184.0       3325.0  FEMALE            Adelie
28      Dream            36.2           17.3              187.0       3300.0  FEMALE            Adelie
29     Biscoe            45.3           13.8              208.0       4200.0  FEMALE            Gentoo
30      Dream            42.4           17.3              181.0       3600.0  FEMALE            Adelie
31     Biscoe            48.8           16.2              222.0       6000.0    MALE            Gentoo
32      Dream            40.2           17.1              193.0       3400.0  FEMALE            Adelie
33     Biscoe            48.1           15.1              209.0       5500.0    MALE            Gentoo
34     Biscoe            47.3           15.3              222.0       5250.0    MALE            Gentoo
35     Biscoe            35.7           16.9              185.0       3150.0  FEMALE            Adelie
36     Biscoe            39.0           17.5              186.0       3550.0  FEMALE            Adelie
37      Dream            46.4           17.8              191.0       3700.0  FEMALE         Chinstrap
38      Dream            45.5           17.0              196.0       3500.0  FEMALE         Chinstrap
39     Biscoe            45.2           14.8              212.0       5200.0  FEMALE            Gentoo
40      Dream            46.2           17.5              187.0       3650.0  FEMALE         Chinstrap
41      Dream            50.6           19.4              193.0       3800.0    MALE         Chinstrap
42     Biscoe            36.4           17.1              184.0       2850.0  FEMALE            Adelie
43     Biscoe            34.5           18.1              187.0       2900.0  FEMALE            Adelie
44     Biscoe            45.1           14.5              215.0       5000.0  FEMALE            Gentoo
45     Biscoe            48.7           15.7              208.0       5350.0    MALE            Gentoo
46     Biscoe            40.6           18.6              183.0       3550.0    MALE            Adelie
47      Dream            45.9           17.1              190.0       3575.0  FEMALE         Chinstrap
48     Biscoe            54.3           15.7              231.0       5650.0    MALE            Gentoo
49      Dream            50.8           18.5              201.0       4450.0    MALE         Chinstrap
50     Biscoe            52.5           15.6              221.0       5450.0    MALE            Gentoo
51     Biscoe            50.5           15.9              222.0       5550.0    MALE            Gentoo
52     Biscoe            49.4           15.8              216.0       4925.0    MALE            Gentoo
53      Dream            45.4           18.7              188.0       3525.0  FEMALE         Chinstrap
54      Dream            35.6           17.5              191.0       3175.0  FEMALE            Adelie
55      Dream            45.2           17.8              198.0       3950.0  FEMALE         Chinstrap
56     Biscoe            39.7           18.9              184.0       3550.0    MALE            Adelie
57      Dream            39.6           18.1              186.0       4450.0    MALE            Adelie
58     Biscoe            46.1           13.2              211.0       4500.0  FEMALE            Gentoo
59  Torgersen            41.5           18.3              195.0       4300.0    MALE            Adelie
60     Biscoe            49.9           16.1              213.0       5400.0    MALE            Gentoo
61     Biscoe            35.3           18.9              187.0       3800.0  FEMALE            Adelie
62      Dream            50.9           19.1              196.0       3550.0    MALE         Chinstrap
63  Torgersen            37.2           19.4              184.0       3900.0    MALE            Adelie
64     Biscoe            39.7           17.7              193.0       3200.0  FEMALE            Adelie
65     Biscoe            45.5           15.0              220.0       5000.0    MALE            Gentoo
66     Biscoe            38.1           17.0              181.0       3175.0  FEMALE            Adelie
```

## 4. AI Insights (Ollama)
Status: skipped

Insight unavailable.
