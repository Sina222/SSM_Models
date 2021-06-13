import networkx as nx
from math import sqrt
#network = nx.Graph()   #undirected graph
network = nx.DiGraph() #directed graph
network.add_nodes_from([
(0, {'label': '0_Timisoara',
	  'x': 21.22722,
	  'y': 45.74944,
	  'received_msg': []
}),
(1, {'label': '1_Bucharest',
	  'x': 26.10626,
	  'y': 44.43225,
	  'received_msg': []
}),
(2, {'label': '2_Mainz-Wiesbaden',
	  'x': 8.27111,
	  'y': 50.0,
	  'received_msg': []
}),
(3, {'label': '3_Mannheim',
	  'x': 8.46472,
	  'y': 49.48833,
	  'received_msg': []
}),
(4, {'label': '4_Stuttgart',
	  'x': 9.17702,
	  'y': 48.78232,
	  'received_msg': []
}),
(5, {'label': '5_Nuremberg',
	  'x': 11.06833,
	  'y': 49.44778,
	  'received_msg': []
}),
(6, {'label': '6_Munich',
	  'x': 11.57549,
	  'y': 48.13743,
	  'received_msg': []
}),
(7, {'label': '7_Vienna',
	  'x': 16.37208,
	  'y': 48.20849,
	  'received_msg': []
}),
(8, {'label': '8_Bratislava',
	  'x': 17.10674,
	  'y': 48.14816,
	  'received_msg': []
}),
(9, {'label': '9_Budapest',
	  'x': 19.03991,
	  'y': 47.49801,
	  'received_msg': []
}),
(10, {'label': '10_Milwaukee',
	  'x': -87.90647,
	  'y': 43.0389,
	  'received_msg': []
}),
(11, {'label': '11_Minneapolis',
	  'x': -93.26384,
	  'y': 44.97997,
	  'received_msg': []
}),
(12, {'label': '12_South_Bend',
	  'x': -86.25001,
	  'y': 41.68338,
	  'received_msg': []
}),
(13, {'label': '13_Chicago',
	  'x': -87.65005,
	  'y': 41.85003,
	  'received_msg': []
}),
(14, {'label': '14_Kansas_City',
	  'x': -94.62746,
	  'y': 39.11417,
	  'received_msg': []
}),
(15, {'label': '15_St_Louis',
	  'x': -90.19789,
	  'y': 38.62727,
	  'received_msg': []
}),
(16, {'label': '16_Des_Moines',
	  'x': -93.60911,
	  'y': 41.60054,
	  'received_msg': []
}),
(17, {'label': '17_Omaha',
	  'x': -95.93779,
	  'y': 41.25861,
	  'received_msg': []
}),
(18, {'label': '18_Louisville',
	  'x': -85.75941,
	  'y': 38.25424,
	  'received_msg': []
}),
(19, {'label': '19_Nashville',
	  'x': -86.78444,
	  'y': 36.16589,
	  'received_msg': []
}),
(20, {'label': '20_Gijon',
	  'x': -5.66444,
	  'y': 43.54111,
	  'received_msg': []
}),
(21, {'label': '21_Santander',
	  'x': -3.80444,
	  'y': 43.46472,
	  'received_msg': []
}),
(22, {'label': '22_Vigo',
	  'x': -8.71667,
	  'y': 42.23333,
	  'received_msg': []
}),
(23, {'label': '23_Leon',
	  'x': -5.56667,
	  'y': 42.6,
	  'received_msg': []
}),
(24, {'label': '24_Zaragoza',
	  'x': -0.87734,
	  'y': 41.65606,
	  'received_msg': []
}),
(25, {'label': '25_Barcelona',
	  'x': 2.15899,
	  'y': 41.38879,
	  'received_msg': []
}),
(26, {'label': '26_Bilbao',
	  'x': -2.92528,
	  'y': 43.26271,
	  'received_msg': []
}),
(27, {'label': '27_Logrono',
	  'x': -2.45,
	  'y': 42.46667,
	  'received_msg': []
}),
(28, {'label': '28_Avila',
	  'x': -4.7,
	  'y': 40.65,
	  'received_msg': []
}),
(29, {'label': '29_San_Sebastian',
	  'x': -1.97499,
	  'y': 43.31283,
	  'received_msg': []
}),
(30, {'label': '30_Indianapolis',
	  'x': -86.15804,
	  'y': 39.76838,
	  'received_msg': []
}),
(31, {'label': '31_Cincinnati',
	  'x': -84.45689,
	  'y': 39.162,
	  'received_msg': []
}),
(32, {'label': '32_Toledo',
	  'x': -83.55521,
	  'y': 41.66394,
	  'received_msg': []
}),
(33, {'label': '33_Detroit',
	  'x': -83.04575,
	  'y': 42.33143,
	  'received_msg': []
}),
(34, {'label': '34_Dayton',
	  'x': -84.19161,
	  'y': 39.75895,
	  'received_msg': []
}),
(35, {'label': '35_Columbus',
	  'x': -82.99879,
	  'y': 39.96118,
	  'received_msg': []
}),
(36, {'label': '36_Hamilton',
	  'x': -84.56134,
	  'y': 39.3995,
	  'received_msg': []
}),
(37, {'label': '37_Cleveland',
	  'x': -81.69541,
	  'y': 41.4995,
	  'received_msg': []
}),
(38, {'label': '38_Buffalo',
	  'x': -78.87837,
	  'y': 42.88645,
	  'received_msg': []
}),
(39, {'label': '39_Toronto',
	  'x': -80.60091,
	  'y': 40.46423,
	  'received_msg': []
}),
(40, {'label': '40_Oslo',
	  'x': 10.74609,
	  'y': 59.91273,
	  'received_msg': []
}),
(41, {'label': '41_Stockholm',
	  'x': 18.0649,
	  'y': 59.33258,
	  'received_msg': []
}),
(42, {'label': '42_Copenhagen',
	  'x': 12.56553,
	  'y': 55.67594,
	  'received_msg': []
}),
(43, {'label': '43_Malmo',
	  'x': 13.00073,
	  'y': 55.60587,
	  'received_msg': []
}),
(44, {'label': '44_Newcastle',
	  'x': -1.61396,
	  'y': 54.97328,
	  'received_msg': []
}),
(45, {'label': '45_Leeds',
	  'x': -1.54785,
	  'y': 53.79648,
	  'received_msg': []
}),
(46, {'label': '46_Glasgow',
	  'x': -4.25763,
	  'y': 55.86515,
	  'received_msg': []
}),
(47, {'label': '47_Edinburgh',
	  'x': -3.2,
	  'y': 55.95,
	  'received_msg': []
}),
(48, {'label': '48_Liverpool_Southport',
	  'x': -2.97794,
	  'y': 53.41058,
	  'received_msg': []
}),
(49, {'label': '49_Manchester',
	  'x': -2.23743,
	  'y': 53.48095,
	  'received_msg': []
}),
(50, {'label': '50_Lisbon',
	  'x': -9.13333,
	  'y': 38.71667,
	  'received_msg': []
}),
(51, {'label': '51_Coimbra',
	  'x': -8.41667,
	  'y': 40.2,
	  'received_msg': []
}),
(52, {'label': '52_Alicante',
	  'x': -0.48149,
	  'y': 38.34517,
	  'received_msg': []
}),
(53, {'label': '53_Murcia',
	  'x': -1.11667,
	  'y': 37.98333,
	  'received_msg': []
}),
(54, {'label': '54_Madrid',
	  'x': -3.70256,
	  'y': 40.4165,
	  'received_msg': []
}),
(55, {'label': '55_Valencia',
	  'x': -0.37739,
	  'y': 39.46975,
	  'received_msg': []
}),
(56, {'label': '56_Sevilla',
	  'x': -5.98694,
	  'y': 37.37722,
	  'received_msg': []
}),
(57, {'label': '57_Badajoz',
	  'x': -6.96667,
	  'y': 38.88333,
	  'received_msg': []
}),
(58, {'label': '58_Granada',
	  'x': -3.60667,
	  'y': 37.18817,
	  'received_msg': []
}),
(59, {'label': '59_Malaga',
	  'x': -4.42034,
	  'y': 36.72016,
	  'received_msg': []
}),
(60, {'label': '60_Austin',
	  'x': -97.74306,
	  'y': 30.26715,
	  'received_msg': []
}),
(61, {'label': '61_San_Antonio',
	  'x': -98.49363,
	  'y': 29.42412,
	  'received_msg': []
}),
(62, {'label': '62_New_Orleans',
	  'x': -90.07507,
	  'y': 29.95465,
	  'received_msg': []
}),
(63, {'label': '63_Jackson',
	  'x': -90.18481,
	  'y': 32.29876,
	  'received_msg': []
}),
(64, {'label': '64_Tulsa',
	  'x': -95.99278,
	  'y': 36.15398,
	  'received_msg': []
}),
(65, {'label': '65_Oklahoma_City',
	  'x': -97.51643,
	  'y': 35.46756,
	  'received_msg': []
}),
(66, {'label': '66_Fort_Worth',
	  'x': -97.32085,
	  'y': 32.72541,
	  'received_msg': []
}),
(67, {'label': '67_Dallas',
	  'x': -96.80667,
	  'y': 32.78306,
	  'received_msg': []
}),
(68, {'label': '68_Memphis',
	  'x': -90.04898,
	  'y': 35.14953,
	  'received_msg': []
}),
(69, {'label': '69_Houston',
	  'x': -95.36327,
	  'y': 29.76328,
	  'received_msg': []
}),
(70, {'label': '70_Tours',
	  'x': 0.68333,
	  'y': 47.38333,
	  'received_msg': []
}),
(71, {'label': '71_Nantes',
	  'x': -1.55336,
	  'y': 47.21725,
	  'received_msg': []
}),
(72, {'label': '72_Rennes',
	  'x': -1.68333,
	  'y': 48.08333,
	  'received_msg': []
}),
(73, {'label': '73_Caen',
	  'x': -0.35912,
	  'y': 49.18585,
	  'received_msg': []
}),
(74, {'label': '74_Rouen',
	  'x': 1.09932,
	  'y': 49.44313,
	  'received_msg': []
}),
(75, {'label': '75_Reims',
	  'x': 4.03333,
	  'y': 49.25,
	  'received_msg': []
}),
(76, {'label': '76_Luxembourg',
	  'x': 6.13,
	  'y': 49.61167,
	  'received_msg': []
}),
(77, {'label': '77_Frankfurt',
	  'x': 8.68333,
	  'y': 50.11667,
	  'received_msg': []
}),
(78, {'label': '78_Bordeaux',
	  'x': -0.56667,
	  'y': 44.83333,
	  'received_msg': []
}),
(79, {'label': '79_Poiters',
	  'x': 0.33333,
	  'y': 46.58333,
	  'received_msg': []
}),
(80, {'label': '80_Miami',
	  'x': -80.19366,
	  'y': 25.77427,
	  'received_msg': []
}),
(81, {'label': '81_Boca_Raton',
	  'x': -80.0831,
	  'y': 26.35869,
	  'received_msg': []
}),
(82, {'label': '82_Atlanta',
	  'x': -84.38798,
	  'y': 33.749,
	  'received_msg': []
}),
(83, {'label': '83_Charlotte',
	  'x': -80.84313,
	  'y': 35.22709,
	  'received_msg': []
}),
(84, {'label': '84_Greensboro',
	  'x': -79.79198,
	  'y': 36.07264,
	  'received_msg': []
}),
(85, {'label': '85_Raleigh',
	  'x': -78.63861,
	  'y': 35.7721,
	  'received_msg': []
}),
(86, {'label': '86_Tampa',
	  'x': -82.45843,
	  'y': 27.94752,
	  'received_msg': []
}),
(87, {'label': '87_Orlando',
	  'x': -81.37924,
	  'y': 28.53834,
	  'received_msg': []
}),
(88, {'label': '88_Jacksonville',
	  'x': -81.65565,
	  'y': 30.33218,
	  'received_msg': []
}),
(89, {'label': '89_Birmingham',
	  'x': -86.80249,
	  'y': 33.52066,
	  'received_msg': []
}),
(90, {'label': '90_Nice',
	  'x': 7.26608,
	  'y': 43.70313,
	  'received_msg': []
}),
(91, {'label': '91_Grenoble',
	  'x': 5.71667,
	  'y': 45.16667,
	  'received_msg': []
}),
(92, {'label': '92_Lyon',
	  'x': 4.85,
	  'y': 45.75,
	  'received_msg': []
}),
(93, {'label': '93_Dijon',
	  'x': 5.01667,
	  'y': 47.31667,
	  'received_msg': []
}),
(94, {'label': '94_Toulouse',
	  'x': 1.44367,
	  'y': 43.60426,
	  'received_msg': []
}),
(95, {'label': '95_Montpellier',
	  'x': 3.88333,
	  'y': 43.6,
	  'received_msg': []
}),
(96, {'label': '96_Marseille',
	  'x': 5.4,
	  'y': 43.3,
	  'received_msg': []
}),
(97, {'label': '97_Sophia',
	  'x': 23.32415,
	  'y': 42.69751,
	  'received_msg': []
}),
(98, {'label': '98_Prague',
	  'x': 14.42076,
	  'y': 50.08804,
	  'received_msg': []
}),
(99, {'label': '99_Geneva',
	  'x': 6.14569,
	  'y': 46.20222,
	  'received_msg': []
}),
(100, {'label': '100_Bern',
	  'x': 7.44744,
	  'y': 46.94809,
	  'received_msg': []
}),
(101, {'label': '101_Los_Angeles',
	  'x': -118.24368,
	  'y': 34.05223,
	  'received_msg': []
}),
(102, {'label': '102_Orange_County',
	  'x': -117.85311,
	  'y': 33.78779,
	  'received_msg': []
}),
(103, {'label': '103_San_Francisco',
	  'x': -122.41942,
	  'y': 37.77493,
	  'received_msg': []
}),
(104, {'label': '104_Santa_Clara',
	  'x': -121.95524,
	  'y': 37.35411,
	  'received_msg': []
}),
(105, {'label': '105_Sacramento',
	  'x': -121.4944,
	  'y': 38.58157,
	  'received_msg': []
}),
(106, {'label': '106_Oakland',
	  'x': -122.2708,
	  'y': 37.80437,
	  'received_msg': []
}),
(107, {'label': '107_Salt_Lake_City',
	  'x': -111.89105,
	  'y': 40.76078,
	  'received_msg': []
}),
(108, {'label': '108_Boise',
	  'x': -116.20345,
	  'y': 43.6135,
	  'received_msg': []
}),
(109, {'label': '109_San_Diego',
	  'x': -117.15726,
	  'y': 32.71533,
	  'received_msg': []
}),
(110, {'label': '110_Phoenix',
	  'x': -112.07404,
	  'y': 33.44838,
	  'received_msg': []
}),
(111, {'label': '111_Arezzo',
	  'x': 11.87691,
	  'y': 43.46139,
	  'received_msg': []
}),
(112, {'label': '112_Rome',
	  'x': 12.4839,
	  'y': 41.89474,
	  'received_msg': []
}),
(113, {'label': '113_Odessa',
	  'x': 30.73262,
	  'y': 46.47747,
	  'received_msg': []
}),
(114, {'label': '114_Galati',
	  'x': 28.05,
	  'y': 45.45,
	  'received_msg': []
}),
(115, {'label': '115_Balchik',
	  'x': 28.16667,
	  'y': 43.41667,
	  'received_msg': []
}),
(116, {'label': '116_Constanta',
	  'x': 28.65,
	  'y': 44.18333,
	  'received_msg': []
}),
(117, {'label': '117_Burgas',
	  'x': 27.46781,
	  'y': 42.50606,
	  'received_msg': []
}),
(118, {'label': '118_Varna',
	  'x': 27.91667,
	  'y': 43.21667,
	  'received_msg': []
}),
(119, {'label': '119_Sofia',
	  'x': 23.32415,
	  'y': 42.69751,
	  'received_msg': []
}),
(120, {'label': '120_Kapitan_Andreevo',
	  'x': 26.31667,
	  'y': 41.71667,
	  'received_msg': []
}),
(121, {'label': '121_McAllen',
	  'x': -98.23001,
	  'y': 26.20341,
	  'received_msg': []
}),
(122, {'label': '122_Laredo',
	  'x': -99.50754,
	  'y': 27.50641,
	  'received_msg': []
}),
(123, {'label': '123_Queretaro',
	  'x': -100.38333,
	  'y': 20.6,
	  'received_msg': []
}),
(124, {'label': '124_Monterrey',
	  'x': -100.31667,
	  'y': 25.66667,
	  'received_msg': []
}),
(125, {'label': '125_Mexico_City',
	  'x': -99.12766,
	  'y': 19.42847,
	  'received_msg': []
}),
(126, {'label': '126_Guadalajara',
	  'x': -103.33333,
	  'y': 20.66667,
	  'received_msg': []
}),
(127, {'label': '127_Albuquerque',
	  'x': -106.65114,
	  'y': 35.08449,
	  'received_msg': []
}),
(128, {'label': '128_El_Paso',
	  'x': -106.48693,
	  'y': 31.75872,
	  'received_msg': []
}),
(129, {'label': '129_Denver',
	  'x': -104.9847,
	  'y': 39.73915,
	  'received_msg': []
}),
(130, {'label': '130_Colorado_Springs',
	  'x': -104.82136,
	  'y': 38.83388,
	  'received_msg': []
}),
(131, {'label': '131_Dresden',
	  'x': 13.73832,
	  'y': 51.05089,
	  'received_msg': []
}),
(132, {'label': '132_Basel',
	  'x': 7.6,
	  'y': 47.56667,
	  'received_msg': []
}),
(133, {'label': '133_Strasbourg',
	  'x': 7.75,
	  'y': 48.58333,
	  'received_msg': []
}),
(134, {'label': '134_Milan',
	  'x': 9.18951,
	  'y': 45.46427,
	  'received_msg': []
}),
(135, {'label': '135_Zurich',
	  'x': 8.55,
	  'y': 47.36667,
	  'received_msg': []
}),
(136, {'label': '136_Zagreb',
	  'x': 15.97798,
	  'y': 45.81444,
	  'received_msg': []
}),
(137, {'label': '137_Genoa',
	  'x': 8.93386,
	  'y': 44.40632,
	  'received_msg': []
}),
(138, {'label': '138_Padua-Venice',
	  'x': 12.32667,
	  'y': 45.43861,
	  'received_msg': []
}),
(139, {'label': '139_Ljubljana',
	  'x': 14.50513,
	  'y': 46.05108,
	  'received_msg': []
}),
(140, {'label': '140_Florence',
	  'x': 11.25,
	  'y': 43.76667,
	  'received_msg': []
}),
(141, {'label': '141_Bologna',
	  'x': 11.33875,
	  'y': 44.49381,
	  'received_msg': []
}),
(142, {'label': '142_Berlin',
	  'x': 13.41053,
	  'y': 52.52437,
	  'received_msg': []
}),
(143, {'label': '143_Hamburg',
	  'x': 10.0,
	  'y': 53.55,
	  'received_msg': []
}),
(144, {'label': '144_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(145, {'label': '145_White_Plains',
	  'x': -73.76291,
	  'y': 41.03399,
	  'received_msg': []
}),
(146, {'label': '146_Baltimore',
	  'x': -76.61219,
	  'y': 39.29038,
	  'received_msg': []
}),
(147, {'label': '147_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(148, {'label': '148_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(149, {'label': '149_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(150, {'label': '150_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(151, {'label': '151_Newark',
	  'x': -74.17237,
	  'y': 40.73566,
	  'received_msg': []
}),
(152, {'label': '152_Philadelphia',
	  'x': -75.16379,
	  'y': 39.95234,
	  'received_msg': []
}),
(153, {'label': '153_Harrisburg',
	  'x': -76.88442,
	  'y': 40.2737,
	  'received_msg': []
}),
(154, {'label': '154_Washington',
	  'x': -77.03637,
	  'y': 38.89511,
	  'received_msg': []
}),
(155, {'label': '155_Boston',
	  'x': -71.05977,
	  'y': 42.35843,
	  'received_msg': []
}),
(156, {'label': '156_Providence',
	  'x': -71.41283,
	  'y': 41.82399,
	  'received_msg': []
}),
(157, {'label': '157_Stamford',
	  'x': -73.53873,
	  'y': 41.05343,
	  'received_msg': []
}),
(158, {'label': '158_New_York',
	  'x': -74.00597,
	  'y': 40.71427,
	  'received_msg': []
}),
(159, {'label': '159_Herndon',
	  'x': -77.3861,
	  'y': 38.96955,
	  'received_msg': []
}),
(160, {'label': '160_Pittsburgh',
	  'x': -79.99589,
	  'y': 40.44062,
	  'received_msg': []
}),
(161, {'label': '161_Cologne',
	  'x': 6.95,
	  'y': 50.93333,
	  'received_msg': []
}),
(162, {'label': '162_Dusseldorf',
	  'x': 6.77616,
	  'y': 51.22172,
	  'received_msg': []
}),
(163, {'label': '163_Amsterdam',
	  'x': 4.88969,
	  'y': 52.37403,
	  'received_msg': []
}),
(164, {'label': '164_Cambridge',
	  'x': 0.11667,
	  'y': 52.2,
	  'received_msg': []
}),
(165, {'label': '165_London',
	  'x': -0.12574,
	  'y': 51.50853,
	  'received_msg': []
}),
(166, {'label': '166_Slough',
	  'x': -0.58333,
	  'y': 51.5,
	  'received_msg': []
}),
(167, {'label': '167_Essen',
	  'x': 7.01667,
	  'y': 51.45,
	  'received_msg': []
}),
(168, {'label': '168_Dortmund',
	  'x': 7.45,
	  'y': 51.51667,
	  'received_msg': []
}),
(169, {'label': '169_Munster',
	  'x': 7.62571,
	  'y': 51.96236,
	  'received_msg': []
}),
(170, {'label': '170_Rotterdam',
	  'x': 4.47917,
	  'y': 51.9225,
	  'received_msg': []
}),
(171, {'label': '171_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(172, {'label': '172_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(173, {'label': '173_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(174, {'label': '174_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(175, {'label': '175_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(176, {'label': '176_None',
	  'x': 0.0,
	  'y': 0.0,
	  'received_msg': []
}),
(177, {'label': '177_Dublin',
	  'x': -6.26719,
	  'y': 53.34399,
	  'received_msg': []
}),
(178, {'label': '178_Seattle',
	  'x': -122.33207,
	  'y': 47.60621,
	  'received_msg': []
}),
(179, {'label': '179_Portland',
	  'x': -122.67621,
	  'y': 45.52345,
	  'received_msg': []
}),
(180, {'label': '180_Las_Vegas',
	  'x': -115.13722,
	  'y': 36.17497,
	  'received_msg': []
}),
(181, {'label': '181_Montreal',
	  'x': -73.58781,
	  'y': 45.50884,
	  'received_msg': []
}),
(182, {'label': '182_Tallinn',
	  'x': 24.75353,
	  'y': 59.43696,
	  'received_msg': []
}),
(183, {'label': '183_Paris',
	  'x': 2.3488,
	  'y': 48.85341,
	  'received_msg': []
}),
(184, {'label': '184_Lille',
	  'x': 3.06667,
	  'y': 50.63333,
	  'received_msg': []
}),
(185, {'label': '185_Bremen',
	  'x': 8.80777,
	  'y': 53.07516,
	  'received_msg': []
}),
(186, {'label': '186_Brussels',
	  'x': 4.34878,
	  'y': 50.85045,
	  'received_msg': []
}),
(187, {'label': '187_Antwerp',
	  'x': 4.41667,
	  'y': 51.21667,
	  'received_msg': []
}),
(188, {'label': '188_Porto',
	  'x': -8.61667,
	  'y': 41.15,
	  'received_msg': []
}),
(189, {'label': '189_Helsinki',
	  'x': 24.93545,
	  'y': 60.16952,
	  'received_msg': []
}),
(190, {'label': '190_Kharkiv',
	  'x': 36.25,
	  'y': 50.0,
	  'received_msg': []
}),
(191, {'label': '191_Kiev',
	  'x': 30.5238,
	  'y': 50.45466,
	  'received_msg': []
}),
(192, {'label': '192_Warsaw',
	  'x': 21.01178,
	  'y': 52.22977,
	  'received_msg': []
}),
(193, {'label': '193_Krakow',
	  'x': 19.91667,
	  'y': 50.08333,
	  'received_msg': []
}),
(194, {'label': '194_Brno',
	  'x': 16.60796,
	  'y': 49.19522,
	  'received_msg': []
}),
(195, {'label': '195_Worcester',
	  'x': -2.22001,
	  'y': 52.18935,
	  'received_msg': []
}),
(196, {'label': '196_Albany',
	  'x': -73.75623,
	  'y': 42.65258,
	  'received_msg': []
}),
])
network.add_edges_from([
(0, 176, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_0'
}),
(176, 0, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_1'
}),
(0, 9, {
	'weight': 10,
	'bw': 1000000,
	'delay': 431,
	'label': 'edge_2'
}),
(9, 0, {
	'weight': 10,
	'bw': 1000000,
	'delay': 431,
	'label': 'edge_3'
}),
(1, 8, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1345,
	'label': 'edge_4'
}),
(8, 1, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1345,
	'label': 'edge_5'
}),
(1, 176, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_6'
}),
(176, 1, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_7'
}),
(1, 114, {
	'weight': 10,
	'bw': 1000000,
	'delay': 321,
	'label': 'edge_8'
}),
(114, 1, {
	'weight': 10,
	'bw': 1000000,
	'delay': 321,
	'label': 'edge_9'
}),
(1, 116, {
	'weight': 10,
	'bw': 1000000,
	'delay': 345,
	'label': 'edge_10'
}),
(116, 1, {
	'weight': 10,
	'bw': 1000000,
	'delay': 345,
	'label': 'edge_11'
}),
(1, 175, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_12'
}),
(175, 1, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_13'
}),
(2, 76, {
	'weight': 10,
	'bw': 1000000,
	'delay': 270,
	'label': 'edge_14'
}),
(76, 2, {
	'weight': 10,
	'bw': 1000000,
	'delay': 270,
	'label': 'edge_15'
}),
(2, 77, {
	'weight': 10,
	'bw': 1000000,
	'delay': 58,
	'label': 'edge_16'
}),
(77, 2, {
	'weight': 10,
	'bw': 1000000,
	'delay': 58,
	'label': 'edge_17'
}),
(3, 4, {
	'weight': 10,
	'bw': 1000000,
	'delay': 161,
	'label': 'edge_18'
}),
(4, 3, {
	'weight': 10,
	'bw': 1000000,
	'delay': 161,
	'label': 'edge_19'
}),
(3, 77, {
	'weight': 10,
	'bw': 1000000,
	'delay': 124,
	'label': 'edge_20'
}),
(77, 3, {
	'weight': 10,
	'bw': 1000000,
	'delay': 124,
	'label': 'edge_21'
}),
(4, 6, {
	'weight': 10,
	'bw': 1000000,
	'delay': 322,
	'label': 'edge_22'
}),
(6, 4, {
	'weight': 10,
	'bw': 1000000,
	'delay': 322,
	'label': 'edge_23'
}),
(4, 135, {
	'weight': 10,
	'bw': 1000000,
	'delay': 278,
	'label': 'edge_24'
}),
(135, 4, {
	'weight': 10,
	'bw': 1000000,
	'delay': 278,
	'label': 'edge_25'
}),
(5, 131, {
	'weight': 10,
	'bw': 1000000,
	'delay': 438,
	'label': 'edge_26'
}),
(131, 5, {
	'weight': 10,
	'bw': 1000000,
	'delay': 438,
	'label': 'edge_27'
}),
(5, 6, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_28'
}),
(6, 5, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_29'
}),
(6, 7, {
	'weight': 10,
	'bw': 1000000,
	'delay': 597,
	'label': 'edge_30'
}),
(7, 6, {
	'weight': 10,
	'bw': 1000000,
	'delay': 597,
	'label': 'edge_31'
}),
(7, 8, {
	'weight': 10,
	'bw': 1000000,
	'delay': 96,
	'label': 'edge_32'
}),
(8, 7, {
	'weight': 10,
	'bw': 1000000,
	'delay': 96,
	'label': 'edge_33'
}),
(7, 174, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_34'
}),
(174, 7, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_35'
}),
(8, 194, {
	'weight': 10,
	'bw': 1000000,
	'delay': 208,
	'label': 'edge_36'
}),
(194, 8, {
	'weight': 10,
	'bw': 1000000,
	'delay': 208,
	'label': 'edge_37'
}),
(8, 191, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1677,
	'label': 'edge_38'
}),
(191, 8, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1677,
	'label': 'edge_39'
}),
(8, 9, {
	'weight': 10,
	'bw': 1000000,
	'delay': 273,
	'label': 'edge_40'
}),
(9, 8, {
	'weight': 10,
	'bw': 1000000,
	'delay': 273,
	'label': 'edge_41'
}),
(10, 11, {
	'weight': 10,
	'bw': 1000000,
	'delay': 803,
	'label': 'edge_42'
}),
(11, 10, {
	'weight': 10,
	'bw': 1000000,
	'delay': 803,
	'label': 'edge_43'
}),
(10, 13, {
	'weight': 10,
	'bw': 1000000,
	'delay': 227,
	'label': 'edge_44'
}),
(13, 10, {
	'weight': 10,
	'bw': 1000000,
	'delay': 227,
	'label': 'edge_45'
}),
(11, 16, {
	'weight': 10,
	'bw': 1000000,
	'delay': 632,
	'label': 'edge_46'
}),
(16, 11, {
	'weight': 10,
	'bw': 1000000,
	'delay': 632,
	'label': 'edge_47'
}),
(12, 32, {
	'weight': 10,
	'bw': 1000000,
	'delay': 377,
	'label': 'edge_48'
}),
(32, 12, {
	'weight': 10,
	'bw': 1000000,
	'delay': 377,
	'label': 'edge_49'
}),
(12, 13, {
	'weight': 10,
	'bw': 1000000,
	'delay': 200,
	'label': 'edge_50'
}),
(13, 12, {
	'weight': 10,
	'bw': 1000000,
	'delay': 200,
	'label': 'edge_51'
}),
(12, 30, {
	'weight': 10,
	'bw': 1000000,
	'delay': 359,
	'label': 'edge_52'
}),
(30, 12, {
	'weight': 10,
	'bw': 1000000,
	'delay': 359,
	'label': 'edge_53'
}),
(13, 16, {
	'weight': 10,
	'bw': 1000000,
	'delay': 829,
	'label': 'edge_54'
}),
(16, 13, {
	'weight': 10,
	'bw': 1000000,
	'delay': 829,
	'label': 'edge_55'
}),
(13, 15, {
	'weight': 10,
	'bw': 1000000,
	'delay': 701,
	'label': 'edge_56'
}),
(15, 13, {
	'weight': 10,
	'bw': 1000000,
	'delay': 701,
	'label': 'edge_57'
}),
(14, 64, {
	'weight': 10,
	'bw': 1000000,
	'delay': 588,
	'label': 'edge_58'
}),
(64, 14, {
	'weight': 10,
	'bw': 1000000,
	'delay': 588,
	'label': 'edge_59'
}),
(14, 129, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1490,
	'label': 'edge_60'
}),
(129, 14, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1490,
	'label': 'edge_61'
}),
(14, 15, {
	'weight': 10,
	'bw': 1000000,
	'delay': 649,
	'label': 'edge_62'
}),
(15, 14, {
	'weight': 10,
	'bw': 1000000,
	'delay': 649,
	'label': 'edge_63'
}),
(16, 17, {
	'weight': 10,
	'bw': 1000000,
	'delay': 334,
	'label': 'edge_64'
}),
(17, 16, {
	'weight': 10,
	'bw': 1000000,
	'delay': 334,
	'label': 'edge_65'
}),
(18, 19, {
	'weight': 10,
	'bw': 1000000,
	'delay': 420,
	'label': 'edge_66'
}),
(19, 18, {
	'weight': 10,
	'bw': 1000000,
	'delay': 420,
	'label': 'edge_67'
}),
(18, 30, {
	'weight': 10,
	'bw': 1000000,
	'delay': 291,
	'label': 'edge_68'
}),
(30, 18, {
	'weight': 10,
	'bw': 1000000,
	'delay': 291,
	'label': 'edge_69'
}),
(19, 89, {
	'weight': 10,
	'bw': 1000000,
	'delay': 494,
	'label': 'edge_70'
}),
(89, 19, {
	'weight': 10,
	'bw': 1000000,
	'delay': 494,
	'label': 'edge_71'
}),
(19, 68, {
	'weight': 10,
	'bw': 1000000,
	'delay': 530,
	'label': 'edge_72'
}),
(68, 19, {
	'weight': 10,
	'bw': 1000000,
	'delay': 530,
	'label': 'edge_73'
}),
(19, 82, {
	'weight': 10,
	'bw': 1000000,
	'delay': 581,
	'label': 'edge_74'
}),
(82, 19, {
	'weight': 10,
	'bw': 1000000,
	'delay': 581,
	'label': 'edge_75'
}),
(20, 21, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_76'
}),
(21, 20, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_77'
}),
(20, 23, {
	'weight': 10,
	'bw': 1000000,
	'delay': 179,
	'label': 'edge_78'
}),
(23, 20, {
	'weight': 10,
	'bw': 1000000,
	'delay': 179,
	'label': 'edge_79'
}),
(21, 26, {
	'weight': 10,
	'bw': 1000000,
	'delay': 129,
	'label': 'edge_80'
}),
(26, 21, {
	'weight': 10,
	'bw': 1000000,
	'delay': 129,
	'label': 'edge_81'
}),
(22, 188, {
	'weight': 10,
	'bw': 1000000,
	'delay': 206,
	'label': 'edge_82'
}),
(188, 22, {
	'weight': 10,
	'bw': 1000000,
	'delay': 206,
	'label': 'edge_83'
}),
(22, 23, {
	'weight': 10,
	'bw': 1000000,
	'delay': 440,
	'label': 'edge_84'
}),
(23, 22, {
	'weight': 10,
	'bw': 1000000,
	'delay': 440,
	'label': 'edge_85'
}),
(24, 27, {
	'weight': 10,
	'bw': 1000000,
	'delay': 268,
	'label': 'edge_86'
}),
(27, 24, {
	'weight': 10,
	'bw': 1000000,
	'delay': 268,
	'label': 'edge_87'
}),
(25, 171, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_88'
}),
(171, 25, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_89'
}),
(25, 55, {
	'weight': 10,
	'bw': 1000000,
	'delay': 509,
	'label': 'edge_90'
}),
(55, 25, {
	'weight': 10,
	'bw': 1000000,
	'delay': 509,
	'label': 'edge_91'
}),
(26, 27, {
	'weight': 10,
	'bw': 1000000,
	'delay': 165,
	'label': 'edge_92'
}),
(27, 26, {
	'weight': 10,
	'bw': 1000000,
	'delay': 165,
	'label': 'edge_93'
}),
(26, 28, {
	'weight': 10,
	'bw': 1000000,
	'delay': 547,
	'label': 'edge_94'
}),
(28, 26, {
	'weight': 10,
	'bw': 1000000,
	'delay': 547,
	'label': 'edge_95'
}),
(26, 29, {
	'weight': 10,
	'bw': 1000000,
	'delay': 133,
	'label': 'edge_96'
}),
(29, 26, {
	'weight': 10,
	'bw': 1000000,
	'delay': 133,
	'label': 'edge_97'
}),
(28, 51, {
	'weight': 10,
	'bw': 1000000,
	'delay': 535,
	'label': 'edge_98'
}),
(51, 28, {
	'weight': 10,
	'bw': 1000000,
	'delay': 535,
	'label': 'edge_99'
}),
(28, 54, {
	'weight': 10,
	'bw': 1000000,
	'delay': 151,
	'label': 'edge_100'
}),
(54, 28, {
	'weight': 10,
	'bw': 1000000,
	'delay': 151,
	'label': 'edge_101'
}),
(29, 78, {
	'weight': 10,
	'bw': 1000000,
	'delay': 343,
	'label': 'edge_102'
}),
(78, 29, {
	'weight': 10,
	'bw': 1000000,
	'delay': 343,
	'label': 'edge_103'
}),
(30, 35, {
	'weight': 10,
	'bw': 1000000,
	'delay': 455,
	'label': 'edge_104'
}),
(35, 30, {
	'weight': 10,
	'bw': 1000000,
	'delay': 455,
	'label': 'edge_105'
}),
(31, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 587,
	'label': 'edge_106'
}),
(37, 31, {
	'weight': 10,
	'bw': 1000000,
	'delay': 587,
	'label': 'edge_107'
}),
(32, 33, {
	'weight': 10,
	'bw': 1000000,
	'delay': 147,
	'label': 'edge_108'
}),
(33, 32, {
	'weight': 10,
	'bw': 1000000,
	'delay': 147,
	'label': 'edge_109'
}),
(32, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 264,
	'label': 'edge_110'
}),
(37, 32, {
	'weight': 10,
	'bw': 1000000,
	'delay': 264,
	'label': 'edge_111'
}),
(34, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 481,
	'label': 'edge_112'
}),
(37, 34, {
	'weight': 10,
	'bw': 1000000,
	'delay': 481,
	'label': 'edge_113'
}),
(35, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 343,
	'label': 'edge_114'
}),
(37, 35, {
	'weight': 10,
	'bw': 1000000,
	'delay': 343,
	'label': 'edge_115'
}),
(36, 38, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1026,
	'label': 'edge_116'
}),
(38, 36, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1026,
	'label': 'edge_117'
}),
(36, 39, {
	'weight': 10,
	'bw': 1000000,
	'delay': 600,
	'label': 'edge_118'
}),
(39, 36, {
	'weight': 10,
	'bw': 1000000,
	'delay': 600,
	'label': 'edge_119'
}),
(37, 160, {
	'weight': 10,
	'bw': 1000000,
	'delay': 313,
	'label': 'edge_120'
}),
(160, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 313,
	'label': 'edge_121'
}),
(37, 38, {
	'weight': 10,
	'bw': 1000000,
	'delay': 469,
	'label': 'edge_122'
}),
(38, 37, {
	'weight': 10,
	'bw': 1000000,
	'delay': 469,
	'label': 'edge_123'
}),
(38, 196, {
	'weight': 10,
	'bw': 1000000,
	'delay': 702,
	'label': 'edge_124'
}),
(196, 38, {
	'weight': 10,
	'bw': 1000000,
	'delay': 702,
	'label': 'edge_125'
}),
(39, 181, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1336,
	'label': 'edge_126'
}),
(181, 39, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1336,
	'label': 'edge_127'
}),
(40, 41, {
	'weight': 10,
	'bw': 1000000,
	'delay': 698,
	'label': 'edge_128'
}),
(41, 40, {
	'weight': 10,
	'bw': 1000000,
	'delay': 698,
	'label': 'edge_129'
}),
(40, 42, {
	'weight': 10,
	'bw': 1000000,
	'delay': 809,
	'label': 'edge_130'
}),
(42, 40, {
	'weight': 10,
	'bw': 1000000,
	'delay': 809,
	'label': 'edge_131'
}),
(41, 43, {
	'weight': 10,
	'bw': 1000000,
	'delay': 859,
	'label': 'edge_132'
}),
(43, 41, {
	'weight': 10,
	'bw': 1000000,
	'delay': 859,
	'label': 'edge_133'
}),
(41, 189, {
	'weight': 10,
	'bw': 1000000,
	'delay': 664,
	'label': 'edge_134'
}),
(189, 41, {
	'weight': 10,
	'bw': 1000000,
	'delay': 664,
	'label': 'edge_135'
}),
(42, 43, {
	'weight': 10,
	'bw': 1000000,
	'delay': 52,
	'label': 'edge_136'
}),
(43, 42, {
	'weight': 10,
	'bw': 1000000,
	'delay': 52,
	'label': 'edge_137'
}),
(42, 143, {
	'weight': 10,
	'bw': 1000000,
	'delay': 485,
	'label': 'edge_138'
}),
(143, 42, {
	'weight': 10,
	'bw': 1000000,
	'delay': 485,
	'label': 'edge_139'
}),
(42, 143, {
	'weight': 10,
	'bw': 1000000,
	'delay': 485,
	'label': 'edge_140'
}),
(143, 42, {
	'weight': 10,
	'bw': 1000000,
	'delay': 485,
	'label': 'edge_141'
}),
(44, 45, {
	'weight': 10,
	'bw': 1000000,
	'delay': 223,
	'label': 'edge_142'
}),
(45, 44, {
	'weight': 10,
	'bw': 1000000,
	'delay': 223,
	'label': 'edge_143'
}),
(44, 47, {
	'weight': 10,
	'bw': 1000000,
	'delay': 250,
	'label': 'edge_144'
}),
(47, 44, {
	'weight': 10,
	'bw': 1000000,
	'delay': 250,
	'label': 'edge_145'
}),
(45, 48, {
	'weight': 10,
	'bw': 1000000,
	'delay': 177,
	'label': 'edge_146'
}),
(48, 45, {
	'weight': 10,
	'bw': 1000000,
	'delay': 177,
	'label': 'edge_147'
}),
(45, 164, {
	'weight': 10,
	'bw': 1000000,
	'delay': 354,
	'label': 'edge_148'
}),
(164, 45, {
	'weight': 10,
	'bw': 1000000,
	'delay': 354,
	'label': 'edge_149'
}),
(46, 49, {
	'weight': 10,
	'bw': 1000000,
	'delay': 496,
	'label': 'edge_150'
}),
(49, 46, {
	'weight': 10,
	'bw': 1000000,
	'delay': 496,
	'label': 'edge_151'
}),
(46, 47, {
	'weight': 10,
	'bw': 1000000,
	'delay': 115,
	'label': 'edge_152'
}),
(47, 46, {
	'weight': 10,
	'bw': 1000000,
	'delay': 115,
	'label': 'edge_153'
}),
(48, 155, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8363,
	'label': 'edge_154'
}),
(155, 48, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8363,
	'label': 'edge_155'
}),
(48, 181, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8272,
	'label': 'edge_156'
}),
(181, 48, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8272,
	'label': 'edge_157'
}),
(49, 177, {
	'weight': 10,
	'bw': 1000000,
	'delay': 450,
	'label': 'edge_158'
}),
(177, 49, {
	'weight': 10,
	'bw': 1000000,
	'delay': 450,
	'label': 'edge_159'
}),
(49, 147, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_160'
}),
(147, 49, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_161'
}),
(49, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 440,
	'label': 'edge_162'
}),
(165, 49, {
	'weight': 10,
	'bw': 1000000,
	'delay': 440,
	'label': 'edge_163'
}),
(50, 57, {
	'weight': 10,
	'bw': 1000000,
	'delay': 319,
	'label': 'edge_164'
}),
(57, 50, {
	'weight': 10,
	'bw': 1000000,
	'delay': 319,
	'label': 'edge_165'
}),
(50, 51, {
	'weight': 10,
	'bw': 1000000,
	'delay': 298,
	'label': 'edge_166'
}),
(51, 50, {
	'weight': 10,
	'bw': 1000000,
	'delay': 298,
	'label': 'edge_167'
}),
(51, 188, {
	'weight': 10,
	'bw': 1000000,
	'delay': 183,
	'label': 'edge_168'
}),
(188, 51, {
	'weight': 10,
	'bw': 1000000,
	'delay': 183,
	'label': 'edge_169'
}),
(52, 53, {
	'weight': 10,
	'bw': 1000000,
	'delay': 119,
	'label': 'edge_170'
}),
(53, 52, {
	'weight': 10,
	'bw': 1000000,
	'delay': 119,
	'label': 'edge_171'
}),
(52, 55, {
	'weight': 10,
	'bw': 1000000,
	'delay': 213,
	'label': 'edge_172'
}),
(55, 52, {
	'weight': 10,
	'bw': 1000000,
	'delay': 213,
	'label': 'edge_173'
}),
(53, 58, {
	'weight': 10,
	'bw': 1000000,
	'delay': 398,
	'label': 'edge_174'
}),
(58, 53, {
	'weight': 10,
	'bw': 1000000,
	'delay': 398,
	'label': 'edge_175'
}),
(54, 55, {
	'weight': 10,
	'bw': 1000000,
	'delay': 508,
	'label': 'edge_176'
}),
(55, 54, {
	'weight': 10,
	'bw': 1000000,
	'delay': 508,
	'label': 'edge_177'
}),
(56, 57, {
	'weight': 10,
	'bw': 1000000,
	'delay': 318,
	'label': 'edge_178'
}),
(57, 56, {
	'weight': 10,
	'bw': 1000000,
	'delay': 318,
	'label': 'edge_179'
}),
(56, 59, {
	'weight': 10,
	'bw': 1000000,
	'delay': 266,
	'label': 'edge_180'
}),
(59, 56, {
	'weight': 10,
	'bw': 1000000,
	'delay': 266,
	'label': 'edge_181'
}),
(58, 59, {
	'weight': 10,
	'bw': 1000000,
	'delay': 153,
	'label': 'edge_182'
}),
(59, 58, {
	'weight': 10,
	'bw': 1000000,
	'delay': 153,
	'label': 'edge_183'
}),
(60, 61, {
	'weight': 10,
	'bw': 1000000,
	'delay': 202,
	'label': 'edge_184'
}),
(61, 60, {
	'weight': 10,
	'bw': 1000000,
	'delay': 202,
	'label': 'edge_185'
}),
(60, 69, {
	'weight': 10,
	'bw': 1000000,
	'delay': 397,
	'label': 'edge_186'
}),
(69, 60, {
	'weight': 10,
	'bw': 1000000,
	'delay': 397,
	'label': 'edge_187'
}),
(61, 128, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1350,
	'label': 'edge_188'
}),
(128, 61, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1350,
	'label': 'edge_189'
}),
(61, 122, {
	'weight': 10,
	'bw': 1000000,
	'delay': 396,
	'label': 'edge_190'
}),
(122, 61, {
	'weight': 10,
	'bw': 1000000,
	'delay': 396,
	'label': 'edge_191'
}),
(62, 144, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_192'
}),
(144, 62, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_193'
}),
(62, 86, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1293,
	'label': 'edge_194'
}),
(86, 62, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1293,
	'label': 'edge_195'
}),
(62, 63, {
	'weight': 10,
	'bw': 1000000,
	'delay': 439,
	'label': 'edge_196'
}),
(63, 62, {
	'weight': 10,
	'bw': 1000000,
	'delay': 439,
	'label': 'edge_197'
}),
(63, 68, {
	'weight': 10,
	'bw': 1000000,
	'delay': 533,
	'label': 'edge_198'
}),
(68, 63, {
	'weight': 10,
	'bw': 1000000,
	'delay': 533,
	'label': 'edge_199'
}),
(63, 149, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_200'
}),
(149, 63, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_201'
}),
(64, 65, {
	'weight': 10,
	'bw': 1000000,
	'delay': 266,
	'label': 'edge_202'
}),
(65, 64, {
	'weight': 10,
	'bw': 1000000,
	'delay': 266,
	'label': 'edge_203'
}),
(64, 67, {
	'weight': 10,
	'bw': 1000000,
	'delay': 641,
	'label': 'edge_204'
}),
(67, 64, {
	'weight': 10,
	'bw': 1000000,
	'delay': 641,
	'label': 'edge_205'
}),
(64, 68, {
	'weight': 10,
	'bw': 1000000,
	'delay': 918,
	'label': 'edge_206'
}),
(68, 64, {
	'weight': 10,
	'bw': 1000000,
	'delay': 918,
	'label': 'edge_207'
}),
(65, 66, {
	'weight': 10,
	'bw': 1000000,
	'delay': 513,
	'label': 'edge_208'
}),
(66, 65, {
	'weight': 10,
	'bw': 1000000,
	'delay': 513,
	'label': 'edge_209'
}),
(66, 67, {
	'weight': 10,
	'bw': 1000000,
	'delay': 85,
	'label': 'edge_210'
}),
(67, 66, {
	'weight': 10,
	'bw': 1000000,
	'delay': 85,
	'label': 'edge_211'
}),
(67, 69, {
	'weight': 10,
	'bw': 1000000,
	'delay': 609,
	'label': 'edge_212'
}),
(69, 67, {
	'weight': 10,
	'bw': 1000000,
	'delay': 609,
	'label': 'edge_213'
}),
(69, 144, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_214'
}),
(144, 69, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_215'
}),
(70, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 346,
	'label': 'edge_216'
}),
(183, 70, {
	'weight': 10,
	'bw': 1000000,
	'delay': 346,
	'label': 'edge_217'
}),
(70, 79, {
	'weight': 10,
	'bw': 1000000,
	'delay': 159,
	'label': 'edge_218'
}),
(79, 70, {
	'weight': 10,
	'bw': 1000000,
	'delay': 159,
	'label': 'edge_219'
}),
(71, 72, {
	'weight': 10,
	'bw': 1000000,
	'delay': 166,
	'label': 'edge_220'
}),
(72, 71, {
	'weight': 10,
	'bw': 1000000,
	'delay': 166,
	'label': 'edge_221'
}),
(71, 79, {
	'weight': 10,
	'bw': 1000000,
	'delay': 271,
	'label': 'edge_222'
}),
(79, 71, {
	'weight': 10,
	'bw': 1000000,
	'delay': 271,
	'label': 'edge_223'
}),
(72, 73, {
	'weight': 10,
	'bw': 1000000,
	'delay': 265,
	'label': 'edge_224'
}),
(73, 72, {
	'weight': 10,
	'bw': 1000000,
	'delay': 265,
	'label': 'edge_225'
}),
(73, 74, {
	'weight': 10,
	'bw': 1000000,
	'delay': 187,
	'label': 'edge_226'
}),
(74, 73, {
	'weight': 10,
	'bw': 1000000,
	'delay': 187,
	'label': 'edge_227'
}),
(74, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 191,
	'label': 'edge_228'
}),
(183, 74, {
	'weight': 10,
	'bw': 1000000,
	'delay': 191,
	'label': 'edge_229'
}),
(75, 173, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_230'
}),
(173, 75, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_231'
}),
(75, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 222,
	'label': 'edge_232'
}),
(183, 75, {
	'weight': 10,
	'bw': 1000000,
	'delay': 222,
	'label': 'edge_233'
}),
(76, 173, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_234'
}),
(173, 76, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_235'
}),
(77, 152, {
	'weight': 10,
	'bw': 1000000,
	'delay': 10550,
	'label': 'edge_236'
}),
(152, 77, {
	'weight': 10,
	'bw': 1000000,
	'delay': 10550,
	'label': 'edge_237'
}),
(77, 162, {
	'weight': 10,
	'bw': 1000000,
	'delay': 308,
	'label': 'edge_238'
}),
(162, 77, {
	'weight': 10,
	'bw': 1000000,
	'delay': 308,
	'label': 'edge_239'
}),
(77, 133, {
	'weight': 10,
	'bw': 1000000,
	'delay': 310,
	'label': 'edge_240'
}),
(133, 77, {
	'weight': 10,
	'bw': 1000000,
	'delay': 310,
	'label': 'edge_241'
}),
(78, 94, {
	'weight': 10,
	'bw': 1000000,
	'delay': 355,
	'label': 'edge_242'
}),
(94, 78, {
	'weight': 10,
	'bw': 1000000,
	'delay': 355,
	'label': 'edge_243'
}),
(78, 79, {
	'weight': 10,
	'bw': 1000000,
	'delay': 349,
	'label': 'edge_244'
}),
(79, 78, {
	'weight': 10,
	'bw': 1000000,
	'delay': 349,
	'label': 'edge_245'
}),
(80, 81, {
	'weight': 10,
	'bw': 1000000,
	'delay': 114,
	'label': 'edge_246'
}),
(81, 80, {
	'weight': 10,
	'bw': 1000000,
	'delay': 114,
	'label': 'edge_247'
}),
(80, 81, {
	'weight': 10,
	'bw': 1000000,
	'delay': 114,
	'label': 'edge_248'
}),
(81, 80, {
	'weight': 10,
	'bw': 1000000,
	'delay': 114,
	'label': 'edge_249'
}),
(80, 86, {
	'weight': 10,
	'bw': 1000000,
	'delay': 554,
	'label': 'edge_250'
}),
(86, 80, {
	'weight': 10,
	'bw': 1000000,
	'delay': 554,
	'label': 'edge_251'
}),
(80, 87, {
	'weight': 10,
	'bw': 1000000,
	'delay': 552,
	'label': 'edge_252'
}),
(87, 80, {
	'weight': 10,
	'bw': 1000000,
	'delay': 552,
	'label': 'edge_253'
}),
(82, 88, {
	'weight': 10,
	'bw': 1000000,
	'delay': 769,
	'label': 'edge_254'
}),
(88, 82, {
	'weight': 10,
	'bw': 1000000,
	'delay': 769,
	'label': 'edge_255'
}),
(82, 83, {
	'weight': 10,
	'bw': 1000000,
	'delay': 611,
	'label': 'edge_256'
}),
(83, 82, {
	'weight': 10,
	'bw': 1000000,
	'delay': 611,
	'label': 'edge_257'
}),
(82, 150, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_258'
}),
(150, 82, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_259'
}),
(83, 148, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_260'
}),
(148, 83, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_261'
}),
(84, 148, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_262'
}),
(148, 84, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_263'
}),
(84, 85, {
	'weight': 10,
	'bw': 1000000,
	'delay': 186,
	'label': 'edge_264'
}),
(85, 84, {
	'weight': 10,
	'bw': 1000000,
	'delay': 186,
	'label': 'edge_265'
}),
(86, 87, {
	'weight': 10,
	'bw': 1000000,
	'delay': 212,
	'label': 'edge_266'
}),
(87, 86, {
	'weight': 10,
	'bw': 1000000,
	'delay': 212,
	'label': 'edge_267'
}),
(87, 88, {
	'weight': 10,
	'bw': 1000000,
	'delay': 340,
	'label': 'edge_268'
}),
(88, 87, {
	'weight': 10,
	'bw': 1000000,
	'delay': 340,
	'label': 'edge_269'
}),
(89, 150, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_270'
}),
(150, 89, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_271'
}),
(90, 172, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_272'
}),
(172, 90, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_273'
}),
(91, 99, {
	'weight': 10,
	'bw': 1000000,
	'delay': 204,
	'label': 'edge_274'
}),
(99, 91, {
	'weight': 10,
	'bw': 1000000,
	'delay': 204,
	'label': 'edge_275'
}),
(91, 92, {
	'weight': 10,
	'bw': 1000000,
	'delay': 161,
	'label': 'edge_276'
}),
(92, 91, {
	'weight': 10,
	'bw': 1000000,
	'delay': 161,
	'label': 'edge_277'
}),
(92, 96, {
	'weight': 10,
	'bw': 1000000,
	'delay': 464,
	'label': 'edge_278'
}),
(96, 92, {
	'weight': 10,
	'bw': 1000000,
	'delay': 464,
	'label': 'edge_279'
}),
(92, 93, {
	'weight': 10,
	'bw': 1000000,
	'delay': 295,
	'label': 'edge_280'
}),
(93, 92, {
	'weight': 10,
	'bw': 1000000,
	'delay': 295,
	'label': 'edge_281'
}),
(92, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 659,
	'label': 'edge_282'
}),
(183, 92, {
	'weight': 10,
	'bw': 1000000,
	'delay': 659,
	'label': 'edge_283'
}),
(94, 171, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_284'
}),
(171, 94, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_285'
}),
(95, 96, {
	'weight': 10,
	'bw': 1000000,
	'delay': 216,
	'label': 'edge_286'
}),
(96, 95, {
	'weight': 10,
	'bw': 1000000,
	'delay': 216,
	'label': 'edge_287'
}),
(95, 171, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_288'
}),
(171, 95, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_289'
}),
(96, 97, {
	'weight': 10,
	'bw': 1000000,
	'delay': 2430,
	'label': 'edge_290'
}),
(97, 96, {
	'weight': 10,
	'bw': 1000000,
	'delay': 2430,
	'label': 'edge_291'
}),
(97, 172, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_292'
}),
(172, 97, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_293'
}),
(98, 194, {
	'weight': 10,
	'bw': 1000000,
	'delay': 315,
	'label': 'edge_294'
}),
(194, 98, {
	'weight': 10,
	'bw': 1000000,
	'delay': 315,
	'label': 'edge_295'
}),
(98, 131, {
	'weight': 10,
	'bw': 1000000,
	'delay': 200,
	'label': 'edge_296'
}),
(131, 98, {
	'weight': 10,
	'bw': 1000000,
	'delay': 200,
	'label': 'edge_297'
}),
(99, 100, {
	'weight': 10,
	'bw': 1000000,
	'delay': 220,
	'label': 'edge_298'
}),
(100, 99, {
	'weight': 10,
	'bw': 1000000,
	'delay': 220,
	'label': 'edge_299'
}),
(100, 132, {
	'weight': 10,
	'bw': 1000000,
	'delay': 121,
	'label': 'edge_300'
}),
(132, 100, {
	'weight': 10,
	'bw': 1000000,
	'delay': 121,
	'label': 'edge_301'
}),
(101, 104, {
	'weight': 10,
	'bw': 1000000,
	'delay': 832,
	'label': 'edge_302'
}),
(104, 101, {
	'weight': 10,
	'bw': 1000000,
	'delay': 832,
	'label': 'edge_303'
}),
(101, 180, {
	'weight': 10,
	'bw': 1000000,
	'delay': 618,
	'label': 'edge_304'
}),
(180, 101, {
	'weight': 10,
	'bw': 1000000,
	'delay': 618,
	'label': 'edge_305'
}),
(101, 102, {
	'weight': 10,
	'bw': 1000000,
	'delay': 82,
	'label': 'edge_306'
}),
(102, 101, {
	'weight': 10,
	'bw': 1000000,
	'delay': 82,
	'label': 'edge_307'
}),
(102, 109, {
	'weight': 10,
	'bw': 1000000,
	'delay': 230,
	'label': 'edge_308'
}),
(109, 102, {
	'weight': 10,
	'bw': 1000000,
	'delay': 230,
	'label': 'edge_309'
}),
(103, 104, {
	'weight': 10,
	'bw': 1000000,
	'delay': 108,
	'label': 'edge_310'
}),
(104, 103, {
	'weight': 10,
	'bw': 1000000,
	'delay': 108,
	'label': 'edge_311'
}),
(103, 106, {
	'weight': 10,
	'bw': 1000000,
	'delay': 27,
	'label': 'edge_312'
}),
(106, 103, {
	'weight': 10,
	'bw': 1000000,
	'delay': 27,
	'label': 'edge_313'
}),
(105, 106, {
	'weight': 10,
	'bw': 1000000,
	'delay': 187,
	'label': 'edge_314'
}),
(106, 105, {
	'weight': 10,
	'bw': 1000000,
	'delay': 187,
	'label': 'edge_315'
}),
(105, 107, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1431,
	'label': 'edge_316'
}),
(107, 105, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1431,
	'label': 'edge_317'
}),
(105, 179, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1300,
	'label': 'edge_318'
}),
(179, 105, {
	'weight': 10,
	'bw': 1000000,
	'delay': 1300,
	'label': 'edge_319'
}),
(107, 108, {
	'weight': 10,
	'bw': 1000000,
	'delay': 798,
	'label': 'edge_320'
}),
(108, 107, {
	'weight': 10,
	'bw': 1000000,
	'delay': 798,
	'label': 'edge_321'
}),
(107, 129, {
	'weight': 10,
	'bw': 1000000,
	'delay': 999,
	'label': 'edge_322'
}),
(129, 107, {
	'weight': 10,
	'bw': 1000000,
	'delay': 999,
	'label': 'edge_323'
}),
(108, 179, {
	'weight': 10,
	'bw': 1000000,
	'delay': 928,
	'label': 'edge_324'
}),
(179, 108, {
	'weight': 10,
	'bw': 1000000,
	'delay': 928,
	'label': 'edge_325'
}),
(109, 110, {
	'weight': 10,
	'bw': 1000000,
	'delay': 805,
	'label': 'edge_326'
}),
(110, 109, {
	'weight': 10,
	'bw': 1000000,
	'delay': 805,
	'label': 'edge_327'
}),
(110, 128, {
	'weight': 10,
	'bw': 1000000,
	'delay': 930,
	'label': 'edge_328'
}),
(128, 110, {
	'weight': 10,
	'bw': 1000000,
	'delay': 930,
	'label': 'edge_329'
}),
(111, 112, {
	'weight': 10,
	'bw': 1000000,
	'delay': 306,
	'label': 'edge_330'
}),
(112, 111, {
	'weight': 10,
	'bw': 1000000,
	'delay': 306,
	'label': 'edge_331'
}),
(111, 140, {
	'weight': 10,
	'bw': 1000000,
	'delay': 106,
	'label': 'edge_332'
}),
(140, 111, {
	'weight': 10,
	'bw': 1000000,
	'delay': 106,
	'label': 'edge_333'
}),
(112, 137, {
	'weight': 10,
	'bw': 1000000,
	'delay': 672,
	'label': 'edge_334'
}),
(137, 112, {
	'weight': 10,
	'bw': 1000000,
	'delay': 672,
	'label': 'edge_335'
}),
(113, 114, {
	'weight': 10,
	'bw': 1000000,
	'delay': 399,
	'label': 'edge_336'
}),
(114, 113, {
	'weight': 10,
	'bw': 1000000,
	'delay': 399,
	'label': 'edge_337'
}),
(113, 191, {
	'weight': 10,
	'bw': 1000000,
	'delay': 741,
	'label': 'edge_338'
}),
(191, 113, {
	'weight': 10,
	'bw': 1000000,
	'delay': 741,
	'label': 'edge_339'
}),
(115, 116, {
	'weight': 10,
	'bw': 1000000,
	'delay': 160,
	'label': 'edge_340'
}),
(116, 115, {
	'weight': 10,
	'bw': 1000000,
	'delay': 160,
	'label': 'edge_341'
}),
(115, 118, {
	'weight': 10,
	'bw': 1000000,
	'delay': 55,
	'label': 'edge_342'
}),
(118, 115, {
	'weight': 10,
	'bw': 1000000,
	'delay': 55,
	'label': 'edge_343'
}),
(117, 120, {
	'weight': 10,
	'bw': 1000000,
	'delay': 220,
	'label': 'edge_344'
}),
(120, 117, {
	'weight': 10,
	'bw': 1000000,
	'delay': 220,
	'label': 'edge_345'
}),
(117, 118, {
	'weight': 10,
	'bw': 1000000,
	'delay': 150,
	'label': 'edge_346'
}),
(118, 117, {
	'weight': 10,
	'bw': 1000000,
	'delay': 150,
	'label': 'edge_347'
}),
(119, 176, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_348'
}),
(176, 119, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_349'
}),
(119, 175, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_350'
}),
(175, 119, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_351'
}),
(120, 175, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_352'
}),
(175, 120, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_353'
}),
(121, 122, {
	'weight': 10,
	'bw': 1000000,
	'delay': 325,
	'label': 'edge_354'
}),
(122, 121, {
	'weight': 10,
	'bw': 1000000,
	'delay': 325,
	'label': 'edge_355'
}),
(121, 124, {
	'weight': 10,
	'bw': 1000000,
	'delay': 366,
	'label': 'edge_356'
}),
(124, 121, {
	'weight': 10,
	'bw': 1000000,
	'delay': 366,
	'label': 'edge_357'
}),
(123, 124, {
	'weight': 10,
	'bw': 1000000,
	'delay': 943,
	'label': 'edge_358'
}),
(124, 123, {
	'weight': 10,
	'bw': 1000000,
	'delay': 943,
	'label': 'edge_359'
}),
(123, 125, {
	'weight': 10,
	'bw': 1000000,
	'delay': 312,
	'label': 'edge_360'
}),
(125, 123, {
	'weight': 10,
	'bw': 1000000,
	'delay': 312,
	'label': 'edge_361'
}),
(123, 126, {
	'weight': 10,
	'bw': 1000000,
	'delay': 516,
	'label': 'edge_362'
}),
(126, 123, {
	'weight': 10,
	'bw': 1000000,
	'delay': 516,
	'label': 'edge_363'
}),
(127, 128, {
	'weight': 10,
	'bw': 1000000,
	'delay': 621,
	'label': 'edge_364'
}),
(128, 127, {
	'weight': 10,
	'bw': 1000000,
	'delay': 621,
	'label': 'edge_365'
}),
(127, 130, {
	'weight': 10,
	'bw': 1000000,
	'delay': 750,
	'label': 'edge_366'
}),
(130, 127, {
	'weight': 10,
	'bw': 1000000,
	'delay': 750,
	'label': 'edge_367'
}),
(129, 130, {
	'weight': 10,
	'bw': 1000000,
	'delay': 174,
	'label': 'edge_368'
}),
(130, 129, {
	'weight': 10,
	'bw': 1000000,
	'delay': 174,
	'label': 'edge_369'
}),
(131, 142, {
	'weight': 10,
	'bw': 1000000,
	'delay': 280,
	'label': 'edge_370'
}),
(142, 131, {
	'weight': 10,
	'bw': 1000000,
	'delay': 280,
	'label': 'edge_371'
}),
(132, 135, {
	'weight': 10,
	'bw': 1000000,
	'delay': 129,
	'label': 'edge_372'
}),
(135, 132, {
	'weight': 10,
	'bw': 1000000,
	'delay': 129,
	'label': 'edge_373'
}),
(133, 173, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_374'
}),
(173, 133, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_375'
}),
(134, 137, {
	'weight': 10,
	'bw': 1000000,
	'delay': 203,
	'label': 'edge_376'
}),
(137, 134, {
	'weight': 10,
	'bw': 1000000,
	'delay': 203,
	'label': 'edge_377'
}),
(134, 138, {
	'weight': 10,
	'bw': 1000000,
	'delay': 412,
	'label': 'edge_378'
}),
(138, 134, {
	'weight': 10,
	'bw': 1000000,
	'delay': 412,
	'label': 'edge_379'
}),
(134, 135, {
	'weight': 10,
	'bw': 1000000,
	'delay': 366,
	'label': 'edge_380'
}),
(135, 134, {
	'weight': 10,
	'bw': 1000000,
	'delay': 366,
	'label': 'edge_381'
}),
(136, 139, {
	'weight': 10,
	'bw': 1000000,
	'delay': 199,
	'label': 'edge_382'
}),
(139, 136, {
	'weight': 10,
	'bw': 1000000,
	'delay': 199,
	'label': 'edge_383'
}),
(137, 172, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_384'
}),
(172, 137, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_385'
}),
(138, 174, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_386'
}),
(174, 138, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_387'
}),
(138, 141, {
	'weight': 10,
	'bw': 1000000,
	'delay': 222,
	'label': 'edge_388'
}),
(141, 138, {
	'weight': 10,
	'bw': 1000000,
	'delay': 222,
	'label': 'edge_389'
}),
(139, 174, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_390'
}),
(174, 139, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_391'
}),
(140, 141, {
	'weight': 10,
	'bw': 1000000,
	'delay': 140,
	'label': 'edge_392'
}),
(141, 140, {
	'weight': 10,
	'bw': 1000000,
	'delay': 140,
	'label': 'edge_393'
}),
(142, 143, {
	'weight': 10,
	'bw': 1000000,
	'delay': 429,
	'label': 'edge_394'
}),
(143, 142, {
	'weight': 10,
	'bw': 1000000,
	'delay': 429,
	'label': 'edge_395'
}),
(143, 185, {
	'weight': 10,
	'bw': 1000000,
	'delay': 163,
	'label': 'edge_396'
}),
(185, 143, {
	'weight': 10,
	'bw': 1000000,
	'delay': 163,
	'label': 'edge_397'
}),
(144, 149, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_398'
}),
(149, 144, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_399'
}),
(145, 157, {
	'weight': 10,
	'bw': 1000000,
	'delay': 36,
	'label': 'edge_400'
}),
(157, 145, {
	'weight': 10,
	'bw': 1000000,
	'delay': 36,
	'label': 'edge_401'
}),
(146, 152, {
	'weight': 10,
	'bw': 1000000,
	'delay': 245,
	'label': 'edge_402'
}),
(152, 146, {
	'weight': 10,
	'bw': 1000000,
	'delay': 245,
	'label': 'edge_403'
}),
(146, 154, {
	'weight': 10,
	'bw': 1000000,
	'delay': 100,
	'label': 'edge_404'
}),
(154, 146, {
	'weight': 10,
	'bw': 1000000,
	'delay': 100,
	'label': 'edge_405'
}),
(147, 166, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_406'
}),
(166, 147, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_407'
}),
(147, 177, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_408'
}),
(177, 147, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_409'
}),
(148, 154, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_410'
}),
(154, 148, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_411'
}),
(149, 150, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_412'
}),
(150, 149, {
	'weight': 10,
	'bw': 1000000,
	'delay': 825,
	'label': 'edge_413'
}),
(151, 152, {
	'weight': 10,
	'bw': 1000000,
	'delay': 206,
	'label': 'edge_414'
}),
(152, 151, {
	'weight': 10,
	'bw': 1000000,
	'delay': 206,
	'label': 'edge_415'
}),
(152, 153, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_416'
}),
(153, 152, {
	'weight': 10,
	'bw': 1000000,
	'delay': 255,
	'label': 'edge_417'
}),
(153, 160, {
	'weight': 10,
	'bw': 1000000,
	'delay': 445,
	'label': 'edge_418'
}),
(160, 153, {
	'weight': 10,
	'bw': 1000000,
	'delay': 445,
	'label': 'edge_419'
}),
(153, 154, {
	'weight': 10,
	'bw': 1000000,
	'delay': 261,
	'label': 'edge_420'
}),
(154, 153, {
	'weight': 10,
	'bw': 1000000,
	'delay': 261,
	'label': 'edge_421'
}),
(154, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 10273,
	'label': 'edge_422'
}),
(183, 154, {
	'weight': 10,
	'bw': 1000000,
	'delay': 10273,
	'label': 'edge_423'
}),
(154, 159, {
	'weight': 10,
	'bw': 1000000,
	'delay': 57,
	'label': 'edge_424'
}),
(159, 154, {
	'weight': 10,
	'bw': 1000000,
	'delay': 57,
	'label': 'edge_425'
}),
(155, 195, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8506,
	'label': 'edge_426'
}),
(195, 155, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8506,
	'label': 'edge_427'
}),
(155, 156, {
	'weight': 10,
	'bw': 1000000,
	'delay': 115,
	'label': 'edge_428'
}),
(156, 155, {
	'weight': 10,
	'bw': 1000000,
	'delay': 115,
	'label': 'edge_429'
}),
(155, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8772,
	'label': 'edge_430'
}),
(165, 155, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8772,
	'label': 'edge_431'
}),
(156, 157, {
	'weight': 10,
	'bw': 1000000,
	'delay': 332,
	'label': 'edge_432'
}),
(157, 156, {
	'weight': 10,
	'bw': 1000000,
	'delay': 332,
	'label': 'edge_433'
}),
(157, 158, {
	'weight': 10,
	'bw': 1000000,
	'delay': 95,
	'label': 'edge_434'
}),
(158, 157, {
	'weight': 10,
	'bw': 1000000,
	'delay': 95,
	'label': 'edge_435'
}),
(158, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 9281,
	'label': 'edge_436'
}),
(165, 158, {
	'weight': 10,
	'bw': 1000000,
	'delay': 9281,
	'label': 'edge_437'
}),
(158, 196, {
	'weight': 10,
	'bw': 1000000,
	'delay': 365,
	'label': 'edge_438'
}),
(196, 158, {
	'weight': 10,
	'bw': 1000000,
	'delay': 365,
	'label': 'edge_439'
}),
(158, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 9726,
	'label': 'edge_440'
}),
(183, 158, {
	'weight': 10,
	'bw': 1000000,
	'delay': 9726,
	'label': 'edge_441'
}),
(161, 162, {
	'weight': 10,
	'bw': 1000000,
	'delay': 62,
	'label': 'edge_442'
}),
(162, 161, {
	'weight': 10,
	'bw': 1000000,
	'delay': 62,
	'label': 'edge_443'
}),
(162, 163, {
	'weight': 10,
	'bw': 1000000,
	'delay': 308,
	'label': 'edge_444'
}),
(163, 162, {
	'weight': 10,
	'bw': 1000000,
	'delay': 308,
	'label': 'edge_445'
}),
(162, 167, {
	'weight': 10,
	'bw': 1000000,
	'delay': 55,
	'label': 'edge_446'
}),
(167, 162, {
	'weight': 10,
	'bw': 1000000,
	'delay': 55,
	'label': 'edge_447'
}),
(163, 187, {
	'weight': 10,
	'bw': 1000000,
	'delay': 226,
	'label': 'edge_448'
}),
(187, 163, {
	'weight': 10,
	'bw': 1000000,
	'delay': 226,
	'label': 'edge_449'
}),
(163, 164, {
	'weight': 10,
	'bw': 1000000,
	'delay': 546,
	'label': 'edge_450'
}),
(164, 163, {
	'weight': 10,
	'bw': 1000000,
	'delay': 546,
	'label': 'edge_451'
}),
(165, 177, {
	'weight': 10,
	'bw': 1000000,
	'delay': 776,
	'label': 'edge_452'
}),
(177, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 776,
	'label': 'edge_453'
}),
(165, 181, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8701,
	'label': 'edge_454'
}),
(181, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8701,
	'label': 'edge_455'
}),
(165, 184, {
	'weight': 10,
	'bw': 1000000,
	'delay': 410,
	'label': 'edge_456'
}),
(184, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 410,
	'label': 'edge_457'
}),
(165, 186, {
	'weight': 10,
	'bw': 1000000,
	'delay': 538,
	'label': 'edge_458'
}),
(186, 165, {
	'weight': 10,
	'bw': 1000000,
	'delay': 538,
	'label': 'edge_459'
}),
(166, 170, {
	'weight': 10,
	'bw': 1000000,
	'delay': 591,
	'label': 'edge_460'
}),
(170, 166, {
	'weight': 10,
	'bw': 1000000,
	'delay': 591,
	'label': 'edge_461'
}),
(166, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 605,
	'label': 'edge_462'
}),
(183, 166, {
	'weight': 10,
	'bw': 1000000,
	'delay': 605,
	'label': 'edge_463'
}),
(167, 168, {
	'weight': 10,
	'bw': 1000000,
	'delay': 56,
	'label': 'edge_464'
}),
(168, 167, {
	'weight': 10,
	'bw': 1000000,
	'delay': 56,
	'label': 'edge_465'
}),
(168, 169, {
	'weight': 10,
	'bw': 1000000,
	'delay': 89,
	'label': 'edge_466'
}),
(169, 168, {
	'weight': 10,
	'bw': 1000000,
	'delay': 89,
	'label': 'edge_467'
}),
(169, 185, {
	'weight': 10,
	'bw': 1000000,
	'delay': 250,
	'label': 'edge_468'
}),
(185, 169, {
	'weight': 10,
	'bw': 1000000,
	'delay': 250,
	'label': 'edge_469'
}),
(178, 179, {
	'weight': 10,
	'bw': 1000000,
	'delay': 393,
	'label': 'edge_470'
}),
(179, 178, {
	'weight': 10,
	'bw': 1000000,
	'delay': 393,
	'label': 'edge_471'
}),
(181, 196, {
	'weight': 10,
	'bw': 1000000,
	'delay': 534,
	'label': 'edge_472'
}),
(196, 181, {
	'weight': 10,
	'bw': 1000000,
	'delay': 534,
	'label': 'edge_473'
}),
(182, 189, {
	'weight': 10,
	'bw': 1000000,
	'delay': 141,
	'label': 'edge_474'
}),
(189, 182, {
	'weight': 10,
	'bw': 1000000,
	'delay': 141,
	'label': 'edge_475'
}),
(183, 184, {
	'weight': 10,
	'bw': 1000000,
	'delay': 345,
	'label': 'edge_476'
}),
(184, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 345,
	'label': 'edge_477'
}),
(183, 186, {
	'weight': 10,
	'bw': 1000000,
	'delay': 445,
	'label': 'edge_478'
}),
(186, 183, {
	'weight': 10,
	'bw': 1000000,
	'delay': 445,
	'label': 'edge_479'
}),
(186, 187, {
	'weight': 10,
	'bw': 1000000,
	'delay': 73,
	'label': 'edge_480'
}),
(187, 186, {
	'weight': 10,
	'bw': 1000000,
	'delay': 73,
	'label': 'edge_481'
}),
(190, 191, {
	'weight': 10,
	'bw': 1000000,
	'delay': 688,
	'label': 'edge_482'
}),
(191, 190, {
	'weight': 10,
	'bw': 1000000,
	'delay': 688,
	'label': 'edge_483'
}),
(192, 193, {
	'weight': 10,
	'bw': 1000000,
	'delay': 422,
	'label': 'edge_484'
}),
(193, 192, {
	'weight': 10,
	'bw': 1000000,
	'delay': 422,
	'label': 'edge_485'
}),
(193, 194, {
	'weight': 10,
	'bw': 1000000,
	'delay': 434,
	'label': 'edge_486'
}),
(194, 193, {
	'weight': 10,
	'bw': 1000000,
	'delay': 434,
	'label': 'edge_487'
}),
(195, 196, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8765,
	'label': 'edge_488'
}),
(196, 195, {
	'weight': 10,
	'bw': 1000000,
	'delay': 8765,
	'label': 'edge_489'
}),
])

n_nodes = network.number_of_nodes()
list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table

## Shortest path on: DELAY
#for src in list_nodes:
#    table_d = nx.single_source_dijkstra_path(network, src, weight='delay')
#    network.nodes[src]['table_d'] = table_d
#
## Shortest path on: #HOP
#for src in list_nodes:
#    table_h = nx.single_source_shortest_path(network, src)
#    network.nodes[src]['table_h'] = table_h
#
## Shortest path on: BANDWIDTH
#for src in list_nodes:
#    table_b = nx.single_source_dijkstra_path(network, src, weight='bw')
#    network.nodes[src]['table_b'] = table_b
#
## Shortest path on: PHYSICAL DISTANCE
#for e in network.edges:
#	# physical distance = sqrt( (x1-x2)**2 + (y1-y2)**2 )
#	#               ((         x1             -          x2            )**2+(            y1           -           y2          )**2)
#	phys_dist = round(sqrt((network.nodes[e[0]]['x']-network.nodes[e[1]]['x'])**2+(network.nodes[e[0]]['y']-network.nodes[e[1]]['y'])**2), 3)
#	network.edges[e]['phys_dist'] = phys_dist
#for src in list_nodes:
#    table_phys = nx.single_source_dijkstra_path(network, src, weight='phys_dist')
#    network.nodes[src]['table_phys'] = table_phys
