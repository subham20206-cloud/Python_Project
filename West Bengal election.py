# Python_Proimport pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
raw_data = """
candidate,constituency,party,criminal_cases,education,total_asset,liabilities
Abdul Hai,ONDA,IND,0,8th Pass,160171,0
Abdur Razz,FALTA,INC,2,10th Pass,2650450,0
Abhijit Bha,PURULIA,IND,0,Post Gradu,4439532,375000
Abir Chand,CHHATNA,IND,0,Graduate,809000,0
Adhikari Su,NANDIGRA,BJP,1,Post Gradu,10552749,0
Adhikary N,NANDAKUI,BJP,0,Post Gradu,7793230,0
Aditya Kun,SALTORA,Bahujan M,0,12th Pass,20000,0
Aditya Mal,PURULIA,IND,0,8th Pass,9060000,0
Aditya Mar,KHANAKUL,IND,0,5th Pass,104958,0
Agniswar,BISHNUPU,BJP,1,Graduate,7424649,6814277
Ahammad,MAGRAHA,SUCI(C),0,12th Pass,1562000,28000
Ajay Halda,CANNING,IND,0,8th Pass,8706,0
Ajit Baul,BARUIPUR,BSP,0,8th Pass,1158521,108000
Ajit Maity,PINGLA,AITC,1,12th Pass,8575000,0
Ajit Ray,SONAMUK,CPI(M),0,10th Pass,926792,0
Akhil Giri,RAMNAGA,AITC,1,12th Pass,7091258,0
Akshay Kha,CHANDRAF,SUCI(C),0,Graduate,9789710,0
Akshay Sar,KATULPUR,INC,0,Graduate,175000,0
Akshaya Ki,SALBONI,Amra Bang,0,Post Gradu,57000,0
Alok Mukh,BARJORA,AITC,0,10th Pass,1992033,0
Aloke Jalda,RAIDIGHI,AITC,1,Graduate,33522682,7483333
Aloke Kole,UDAYNAR,INC,0,Graduate,3642000,127000
Amal Kuma,ULUBERIA,IND,0,10th Pass,2358777,0
Amarnath,ONDA,BJP,6,10th Pass,6581000,100000
Ambujaksh,PATASHPU,BJP,0,Graduate,107000000,0
Amitabha,SHYAMPUT,INC,2,Post Gradu,5999167,0
Amitav Na,JAYNAGAR,RPI(A),0,Post Gradu,1220000,0
Amulya Ma,SABANG,BJP,1,Graduate,4047204,0
Ananda Ku,BARUIPUR,IND,0,Illiterate,30026,0
Anandi Tuc,BALARAMF,BSP,0,10th Pass,0,0
Anath Baui,CHHATNA,IND,0,8th Pass,48424,25000
Anil Chand,GOSABA,Revolution,0,Post Gradu,1230915,732000
Animesh M,SALBONI,IND,0,10th Pass,36864,0
Anirban Sa,DHANEKH,INC,0,Graduate,15097446,0
Anjan Jana,GHATAL,SUCI(C),0,Graduate,2839724,0
Antara Bha,PINGLA,BJP,0,Post Gradu,5527937,0
Anupam G,JAGATBALI,BJP,0,Graduate,1648493,200000
Anupam M,BAGNAN,BJP,3,Graduate,15000421,0
Anurup Pal,KANTHI DA,CPI,0,12th Pass,54305,0
Apurba Mc,ONDA,SUCI(C),0,Graduate,262000,0
Apurba Pra,JAYNAGAR,CPI(M),4,Graduate,4959303,0
Arati Paha,RAMNAGA,SUCI(C),0,8th Pass,3568106,0
Archana Sa,JHARGRAM,SUCI(C),0,8th Pass,370338,0
Archita Bid,BISHNUPU,AITC,0,Graduate,9699763,1993402
Ardhendu,BHAGABAN,AITC,0,Graduate,2819318,0
Arnab Adh,UDAYNAR,IND,0,Graduate,163225,0
Arnab Roy,CANNING,BJP,0,Graduate,6627572,0
Arunava SE,BAGNAN,AITC,1,12th Pass,6696240,0
Arup Chak,TALDANGF,AITC,0,Graduate,88251416,39858383
Arup Dash,EGRA,BJP,1,Graduate,3656377,0
Arup Dhara,CHANDRAI,AITC,0,Graduate,7039412,1527905
Arup Kuma,KANTHI DA,BJP,0,Post Gradu,10312786,0
Arup Kuma,ONDA,AITC,0,Graduate,6967775,602553
Arup Kuma,CHANDIPU,IND,0,10th Pass,1017000,0
Ashis Kum,CHANDIPU,CPI(M),0,Graduate,203590,0
Ashok Dal,ULUBERIA,CPI(M),1,5th Pass,253122,0
Ashoke Dir,MOYNA,BJP,0,Graduate,75063577,18865905
Ashoke Ma,GOPIBALLA,IND,2,12th Pass,63097,0
Ashutosh,BAGHMUN,AJSU Party,0,Graduate,3863400,140000
Ashutosh F,JHARGRAN,IND,0,Graduate,6323000,0
Asim Kuma,SONAMUK,IND,0,Graduate,202200,0
Asima Patr,DHANEKH,AITC,0,12th Pass,8460657,0
Asit Kumar,PATHARPR,BJP,2,Graduate,1497406,489000
Asit Mitra,AMTA,INC,1,Graduate,1141000,40000
Asoktaru P,BHAGABAN,SUCI(C),0,Others,901500,0
Aswini Sing,BALARAMF,IND,0,10th Pass,88172,0
Atal Kumar,FALTA,BSP,0,12th Pass,2585210,0
Atanu Sam,KHANAKUL,IND,0,8th Pass,8390402,848890
Atta Surja,NARAYANC,AITC,0,Post Gradu,12280040,4000000
Avijit Das,ULUBERIA,IND,0,10th Pass,1302424,0
Avranil Ma,SONAMUK,SUCI(C),0,Graduate,94900,0
Babita Bou,PARA,IND,0,10th Pass,1630000,0
Bablu Gora,BARJORA,Bahujan M,0,12th Pass,30000,0
Bablu Hald,RAIDIGHI,IND,0,Graduate,2107551,691995
Bablu Mur,BINPUR,Jharkhand,0,12th Pass,7000,0
Bablu Sanf,KULTALI,LJP,0,Post Gradu,300500,0
Bahadur KI,JOYPUR,IND,0,10th Pass,897798,0
Baidyanath,BANKURA,IND,0,Graduate,110000,0
Baidyanath,BISHNUPU,IND,0,Post Gradu,3145000,0
Bakul Mur,NAYAGRAM,BJP,0,Post Gradu,8113020,0
Banamali,NARAYANC,IND,0,8th Pass,1926000,1450000
Banamali,GOPIBALLA,BSP,0,8th Pass,27500,0
Baneswar,BALARAMF,BJP,3,12th Pass,3030000,0
Bankim Ch,SAGAR,AITC,0,Post Gradu,9090193,0
Bankim Ch,ARAMBAG,BSP,0,Graduate,3512500,370000
Barsha Ma,KHARAGPL,Amra Bang,0,8th Pass,174100,14000
Barun Prar,GOSABA,BJP,27,Graduate,17854032,17000000
Basudeb Si,BISHNUPU,Bahujan M,0,12th Pass,2966137,680000
Besra Susa,BANDWAN,CPI(M),0,Post Gradu,3560372,2338640
Bhagirath,JOYPUR,SUCI(C),0,12th Pass,0,0
Bharati Gh,DEBRA,BJP,19,Post Gradu,192000000,7798626
Bhim Patra,TAMLUK,IND,0,Literate,256200,0
Bidhan Cha,NAYAGRAM,IND,0,8th Pass,21900,0
Bidhan Par,FALTA,BJP,5,12th Pass,255317,0
Bikash Cha,CHANDIPU,West Beng,0,Post Gradu,1713769,1036577
Bikash Pat,ONDA,CPI(ML),0,10th Pass,79700,0
Bikram Cha,DANTAN,AITC,2,12th Pass,1691439,101437
Bikram Cha,MAHISHAC,Rashtriya S,0,Post Gradu,649130,0
Bimal Poria,PANSKURA,Amra Bang,0,12th Pass,264494,0
Biman Ban,BARUIPUR,AITC,0,Post Gradu,23862266,0
Biman Ghc,PURSURAH,BJP,2,Graduate,210379,0
Biplab Bara,MOYNA,IND,0,Post Gradu,2663860,1416800
Biplab Roy,PANSKURA,AITC,0,12th Pass,3581403,0
Birbaha Ha,JHARGRAM,AITC,0,Graduate,306215,0
Birendrana,PURULIA,IND,0,10th Pass,260700,0
Bishwajit,MEDINIPU,IND,0,10th Pass,60500,0
Biswajit Bis,MAGRAHA,IND,0,12th Pass,10900,0
Biswajit MI,BASANTI,IND,3,8th Pass,337323,0
Biswajit Sa,DIAMOND,IND,0,10th Pass,15000,0
Biswanath,MAHISHAC,BJP,5,10th Pass,2105687,201148
Biswanath,KANTHI UT,Indian Unit,0,8th Pass,1441200,75000
Biswanath,JAYNAGAR,AITC,0,Post Gradu,10789846,1458616
Biswanath,AMTA,IND,0,10th Pass,825865,0
Biswanath,CHANDIPU,BSP,0,12th Pass,22000,1050000
Biswanath,HARIPAL,SUCI(C),0,12th Pass,602512,0
Biswanath,GOGHAT,BJP,8,12th Pass,2532687,0
Biswanath,RANIBAND,IND,0,Graduate,2177500,688000
Bivas Sarda,BARUIPUR,AITC,1,12th Pass,7692159,2438000
Bouri Haza,RAGHUNA,AITC,0,Graduate,1311200,740000
Bouri Parin,RAGHUNA,BSP,0,10th Pass,1074000,0
Chandan K,MAGRAHA,BJP,0,Post Gradu,1740258,0
Chandan,BARUIPUR,BJP,0,10th Pass,26713000,4250000
Chandan P,SATGACHH,BJP,0,12th Pass,31010125,340148
Chandan S,MAGRAHA,CPI(M),1,Post Gradu,717447,250000
Chandan S,KHANAKUL,IND,0,10th Pass,28208347,600000
Chandana,SALTORA,BJP,0,10th Pass,62296,0
Chandram,PANSKURA,SUCI(C),1,12th Pass,830083,0
Chinmay N,BARUIPUR,IND,2,10th Pass,251500,0
Chiran Ber,ULUBERIA,BJP,4,10th Pass,1553,0
Chiranjib B,SABANG,INC,0,Graduate,30199448,2000268
Chiranjit B,PURSURAH,IND,3,10th Pass,5275650,0
Chittaranja,PANSKURA,CPI,2,Post Gradu,6198955,800000
D. Madhus,KHARAGPL,Humanity I,0,10th Pass,3666000,2000000
Debabrata,BASANTI,IND,0,Graduate,5673649,12000
Debabrata,PANSKURA,BJP,1,Post Gradu,5569157,1826790
Debajyoti,SATGACHH,IND,0,Graduate,1644930,0
Debashis B,SABANG,Amra Bang,0,12th Pass,127000,0
Debasis Da,KANTHI UT,IND,2,12th Pass,356000,0
Debasish A,MEDINIPU,SUCI(C),0,Post Gradu,10059604,409960
Debjit Sark,JANGIPAR,BJP,11,Graduate,5195183,304854
Deblina He,RANIBAND,CPI(M),1,10th Pass,1893732,45000
Debnath H,BINPUR,AITC,0,8th Pass,364500,0
Debopam,BARUIPUR,BJP,2,Graduate,1526057,155846
Debranjan,BAGHMUN,AIFB,0,Post Gradu,1100671,0
Debtanu B,AMTA,BJP,2,Graduate,289770,0
Debu Chat,BISHNUPU,INC,0,Graduate,5744507,0
Deepak Ra,FALTA,IND,0,10th Pass,24000,0
Dhirendra,JOYPUR,AIFB,0,8th Pass,1158364,0
Dhruba Sel,DASPUR,CPI(M),0,10th Pass,2750983,2123345
Dhurjati Sa,MAGRAHA,BJP,0,Graduate,5764132,0
Dibakar Gh,SONAMUK,BJP,0,8th Pass,497000,0
Dibakar Ha,BINPUR,CPI(M),0,12th Pass,1334236,4000
Dibya Joti,JOYPUR,IND,0,10th Pass,22243,0
Dilip Kuma,AMTA,IND,0,Post Gradu,980900,500000
Dilip Kuma,MANDIRBA,BJP,9,12th Pass,6810000,60000
Dilip Monc,BISHNUPU,AITC,1,12th Pass,15903820,5505267
Dilip Yadav,PURSURAH,AITC,1,10th Pass,18062199,3152281
Dinabandh,CHHATNA,Bahujan M,0,12th Pass,370000,0
Dinanath C,CHHATNA,IND,0,12th Pass,6491916,0
Dinen Roy,KHARAGPL,AITC,13,12th Pass,37019486,0
Dipak Kum,BALARAMF,SUCI (C),0,12th Pass,0,0
Dipak Kum,NANDIGRA,IND,0,Graduate,1269434,650000
Dipak Kum,DIAMOND,BJP,4,Graduate,10462970,85292
Dipak Kum,KASHIPUR,SUCI(C),0,Graduate,774168,300000
Dipankar Ji,KAKDWIP,BJP,2,Graduate,144000000,42686883
Dipankar N,DEBRA,SUCI(C),0,Graduate,469000,0
Dipen Baur,SALTORA,SUCI(C),0,10th Pass,156500,0
Dr. Karabi,HARIPAL,AITC,0,Others,21104407,1368413
Dr. Khagen,GOPIBALLA,AITC,0,Graduate,8871800,804081
Dr. Nirmal,ULUBERIA,AITC,2,Post Gradu,8435790,381835
Dr. Pulin Bi,KESHIARY,CPI(M),1,Graduate,9344011,0
Dr. Shyama,SONAMUK,AITC,0,Doctorate,6023310,2471586
Dulal Murr,NAYAGRAM,AITC,0,Post Gradu,12035096,0
Faisal Khar,KHANAKUL,Rashtriya S,0,5th Pass,469350,0
Falguni Mu,CHHATNA,Revolution,1,12th Pass,552503,0
Fulchand,RANIBAND,Bahujan M,0,Graduate,111000,0
Ganesh Bo,RAGHUNA,CPI(M),0,Graduate,495506,300000
Ganesh Ch,ULUBERIA,IND,0,12th Pass,2182008,634000
Ganesh Ch,KULTALI,AITC,0,Graduate,63301383,12392528
Gazi Shaha,CANNING,Rashtriya S,0,Post Gradu,234253,169423
Ghosh Susi,SALBONI,CPI(M),6,10th Pass,3881988,0
Gias Uddin,MAGRAHA,AITC,0,8th Pass,15716054,6363282
Gobardhar,JAGATBALI,Indian Unit,0,8th Pass,1343800,0
Gobinda M,KULTALI,IND,1,Graduate,11498500,1220000
Golam Ali,DIAMOND,BSP,0,12th Pass,3706952,0
Gopal Char,CANNING,IND,0,12th Pass,13000,0
Gouranga,CHANDRAI,Rashtriya S,0,Post Gradu,9893533,0
Gouri Sing,MANBAZAI,BJP,0,10th Pass,628255,0
Goutam KL,RANIBAND,SUCI (C),1,Post Gradu,1949000,735000
Goutam Pa,SATGACHH,CPI(M),0,Post Gradu,5382739,0
Goutam Pa,TAMLUK,CPI,0,Graduate,1439664,0
Gunasindh,RAIDIGHI,SUCI(C),5,8th Pass,841237,0
Habul Kum,MAGRAHA,IND,0,Graduate,1140000,0
Haji Mursic,MAGRAHA,IND,3,10th Pass,3265000,0
Hamlet Ba,JHARGRAM,IND,0,12th Pass,208000,0
Harakali Pr,KATULPUR,BJP,0,Post Gradu,6641745,3500000
Haran Bisu,MAGRAHA,Party for D,0,10th Pass,450000,0
Hare Krish,TAMLUK,BJP,0,Doctorate,54000643,0
Harekrishn,SABANG,SUCI (C),0,Others,3974500,0
Harendra,PURULIA,Amra Bang,0,8th Pass,1215000,0
Haripada,BANKURA,IND,0,Post Gradu,4300227,0
Haripada N,GOSABA,BSP,1,Others,2675849,90000
Haripada S,NAYAGRAM,CPI(M),0,Graduate,1601822,194328
Haru Roy,KATULPUR,BSP,1,Post Gradu,1000,0
Himangshu,KHEJURI,CPI(M),24,10th Pass,4201949,0
Hiranmoy,KHARAGPL,BJP,2,Graduate,43710836,6093221
Hulu Kshet,BANKURA,Bahujan M,0,10th Pass,21031,0
Humayun I,DEBRA,AITC,0,Doctorate,27577829,0
Ibrahim Ali,PANSKURA,CPI(M),5,Graduate,1114686,0
Indranil Ro,KAKDWIP,INC,0,Graduate,50504500,0
Jagadis Sau,EGRA,SUCI(C),2,Post Gradu,9187410,0
Jagadish M,DASPUR,SUCI (C),0,12th Pass,561653,0
Jagannath,PARA,SUCI(C),0,Graduate,457500,0
Jawahar La,JOYPUR,Mulnibasi,1,Graduate,465554,40000
Jayanta Kh,ULUBERIA,SUCI(C),0,Graduate,668955,955110
Jayanta Na,GOSABA,AITC,1,8th Pass,21111705,0
Jaykrishna,KULTALI,SUCI(C),2,10th Pass,20600,0
Jhantu Mai,KAKDWIP,SUCI(C),0,Post Gradu,3044503,0
Jhareswar,KESHIARY,SUCI(C),0,8th Pass,431695,0
Jhuma Kay,BISHNUPU,CPI(M),0,12th Pass,3444472,0
Jiten Giri,GOPIBALL,IND,1,5th Pass,36200,0
Jnananand,TAMLUK,SUCI (C),2,Graduate,8570137,950000
Jogaranjan,KULPI,AITC,0,Graduate,12990857,115643
Joydeb Hal,MANDIRBA,AITC,2,10th Pass,3585560,0
Joydev Nas,BARUIPUR,SUCI(C),0,Post Gradu,1768470,0
Julfikar Sha,FALTA,IND,0,8th Pass,13500,0
June Malia,MEDINIPU,AITC,0,12th Pass,34449609,0
Jyotirmoy,KANTHI DA,AITC,0,Graduate,11673924,0
Jyotsna Ma,RANIBAND,AITC,0,Others,4101144,234000
Kalicharan,NAYAGRAM,SUCI(C),0,8th Pass,445500,0
Kalipada,SHYAMPUI,AITC,0,Graduate,8383967,0
Kalipada N,CANNING,BJP,1,8th Pass,1654671,80000
Kamal Bag,MOYNA,BSP,0,10th Pass,10000,0
Kamal Cha,GHATAL,CPI(M),0,Post Gradu,1608530,520000
Kamalakan,KASHIPUR,BJP,0,Post Gradu,4502009,1300000
Kamila Bik,SAGAR,BJP,2,Post Gradu,331589,0
Kanan Bala,KULTALI,BSP,0,10th Pass,2658785,0
Kanti Gang,RAIDIGHI,CPI(M),1,Graduate,3080689,375800
Kar Paik M,HALDIA,CPI(M),0,Post Gradu,9526480,1893546
Kartick Mo,KULTALI,Bahujan M,0,Post Gradu,960000,0
Karuna Sar,NANDAKUI,CPI(M),0,10th Pass,2271348,55000
Kishor Kun,DIAMOND,IND,0,10th Pass,66500,0
Koushik Da,MAHISHAC,IND,0,12th Pass,226300,0
Krishna Ch,ONDA,IND,0,12th Pass,901318,0
Kshudiram,RANIBAND,BJP,0,Graduate,1325600,400000
Kutubuddi,GARBETA,IND,0,5th Pass,22000,52000
Laksmi Kar,SALBONI,IND,0,Graduate,15000,0
Latab Uddi,DIAMOND,IND,0,10th Pass,2327000,0
Laxman Ha,JHARGRAM,Amra Bang,0,Graduate,7073,0
Lina Ghosh,BANKURA,SUCI(C),0,Graduate,1386500,0
Lirika Muki,KANTHI UT,IND,0,12th Pass,3105591,3945078
M. Raquibi,FALTA,IND,0,10th Pass,21000,0
Madan Rui,GARBETA,BJP,0,10th Pass,76176,50000
Madhuja S,JHARGRAM,CPI(M),3,Post Gradu,1138011,0
Madhusud,ARAMBAG,BJP,1,Post Gradu,4951884,2043796
Madhusud,JHARGRAM,IND,1,8th Pass,8851446,0
Mahamma,MOYNA,IND,0,10th Pass,1114000,0
Maidul Isla,MAGRAHA,Rashtriya S,7,Graduate,425013,0
Mallika Ma,KASHIPUR,CPI(M),0,Graduate,3388050,0
Mamata B,NANDIGRA,AITC,0,Post Gradu,1672352,0
Mamata BI,DASPUR,AITC,0,10th Pass,596196,0
Manas Kur,EGRA,INC,3,Graduate,11818457,798304
Manas Ma,GOGHAT,AITC,0,Graduate,1019380,0
Manas Ran,SABANG,AITC,0,Graduate,73494125,26000
Manas Sari,PURULIA,BSP,0,8th Pass,0,0
Mangal Ch,BINPUR,SHS,0,Graduate,505516,0
Manik Bha,MOYNA,INC,2,Graduate,482837,252000
Manik Cha,KHARAGPL,SUCI (C),0,Graduate,761000,0
Manoj Kun,NANDIGRA,SUCI(C),0,10th Pass,1002000,35000
Manoranja,TALDANGF,CPI(M),3,12th Pass,4119000,0
Manturam,KAKDWIP,AITC,2,10th Pass,6707089,0
Marphat A,NANDAKUI,IND,0,Literate,220000,0
Maya Bag,CANNING,IND,0,10th Pass,1212444,400000
Md Lahek,BARUIPUR,CPI(M),0,Post Gradu,560903,118000
Md. Kabiru,SALBONI,Humanity I,3,Graduate,637000,230000
Meghnath,CANNING,IND,0,Post Gradu,9721848,0
Mihir Baur,RAGHUNA,IND,0,12th Pass,1503900,0
Milan Dhui,FALTA,IND,0,8th Pass,5050,0
Milan Man,RAIPUR,Rashtriya S,5,10th Pass,312000,0
Minakshi,NANDIGRA,CPI(M),2,Post Gradu,132198,0
Mintu Halc,KULTALI,BJP,2,8th Pass,569600,20000
Mintu Mist,RAIDIGHI,BSP,0,Graduate,8541415,0
Mithun Ma,KESHIARY,BSP,0,12th Pass,10139,0
Mohan Chi,SATGACHH,AITC,0,Graduate,2518517,0
Mohan Sar,KATULPUR,SUCI(C),0,Literate,301000,0
Monarama,DIAMOND,SUCI(C),0,Post Gradu,13000,0
Mongal Na,MANDIRB,RPI(A),0,12th Pass,260500,0
Monika Ma,PURSURAH,INC,0,Graduate,2795296,1250023
Monotosh,JAYNAGAR,Bahujan M,0,Graduate,2511000,0
Mrinmay,KULPI,IND,0,Graduate,3567406,0
Mritunjoy,PURULIA,IND,1,12th Pass,8451448,50000
Mrityunjoy,RAIPUR,AITC,0,10th Pass,1018005,0
Mrityunjoy,BAGHMUN,SUCI(C),0,Post Gradu,2124000,0
Mukul Mo,BARUIPUR,IND,0,Doctorate,2386822,0
Munsi Naz,KHANAKUL,AITC,9,Graduate,21674345,1976977
Nadiar Cha,PARA,BJP,0,12th Pass,1689675,650000
Nageswar,JOYPUR,IND,0,8th Pass,1930000,0
Namita Sal,MAGRAHA,AITC,0,Graduate,4286392,0
Nandadula,SALTORA,CPI(M),0,Graduate,470077,0
Nara Hari,JOYPUR,BJP,3,Post Gradu,11727000,200000
Narayan H,PATHARPR,SUCI(C),0,12th Pass,5017602,0
Narayan Ki,PANSKURA,IND,1,Post Gradu,144615,0
Narayan N,CANNING,SUCI(C),0,Graduate,4686313,0
Narayan Pr,HALDIA,SUCI(C),0,12th Pass,711542,0
Narendra,KASHIPUR,Amra Bang,0,Post Gradu,800500,0
Nayan Kun,INDUS,CPI(M),0,Graduate,51047,22000
Nepal Char,BAGHMUN,INC,2,Post Gradu,5097439,419982
Nepal Char,JOYPUR,IND,0,10th Pass,1819640,242757
Niladri Sek,BANKURA,BJP,0,12th Pass,19001000,0
Nimai Char,BASANTI,SUCI(C),0,12th Pass,4064000,0
Nirapada,ULUBERIA,IND,0,12th Pass,413773,0
Nirmal,ONDA,CPI(ML),0,8th Pass,141262,0
Nirmal Kur,INDUS,BJP,0,Post Gradu,1700,0
Nityalal Sir,BINPUR,IND,0,12th Pass,706577,0
Pabitra Hal,MANDIRBA,IND,0,Post Gradu,828300,0
Palan Sare,BINPUR,BJP,2,10th Pass,1050135,670980
Palash Halo,MAGRAHA,IND,0,8th Pass,175637,93000
Pampa Sar,BAGNAN,SUCI(C),0,Graduate,3107070,0
Panchanan,KANTHI UT,SUCI(C),1,12th Pass,706650,0
Panchanan,JAGATBALL,IND,0,12th Pass,3000,0
Pannalal H,DIAMOND,AITC,0,Graduate,59450472,0
Papia Dey,ULUBERIA,BJP,0,Post Gradu,23053825,4471647
Parbati Bhi,KAKDWIP,BSP,0,8th Pass,440480,0
Parcy Mur,BANDWAN,BJP,0,12th Pass,1208827,836558
Paresh Cha,SALBONI,SUCI(C),0,Post Gradu,1828481,1200000
Paresh Mu,KESHIARY,AITC,0,Graduate,4010329,0
Paresh Rar,CANNING,AITC,9,12th Pass,5656988,1500000
Partha Hal,MANDIRB,Bahujan M,0,Graduate,20500,0
Partha Pra,PURULIA,INC,0,Graduate,19538621,952289
Partha Pra,KHEJURI,AITC,10,Graduate,6536726,4000000
Pashupati,BAGHMUN,Amra Bang,0,Graduate,716000,0
"""
df = pd.read_csv(StringIO(raw_data))
features = ['criminal_cases', 'education', 'total_asset', 'liabilities']
target = 'party'
X = df[features]
y = df[target]
numerical_features = ['criminal_cases', 'total_asset', 'liabilities']
categorical_features = ['education']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])
model_pipeline.fit(X_train, y_train)
y_pred = model_pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
