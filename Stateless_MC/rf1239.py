import networkx as nx
#network = nx.Graph()   #undirected graph
network = nx.DiGraph() #directed graph
network.add_nodes_from([
(0, {'label': 'San+Jose,+CA4062',
	  'received_msg': []
}),
(1, {'label': 'Anaheim,+CA4101',
	  'received_msg': []
}),
(2, {'label': 'San+Jose,+CA4119',
	  'received_msg': []
}),
(3, {'label': 'Tacoma,+WA3251',
	  'received_msg': []
}),
(4, {'label': 'Relay,+MD4110',
	  'received_msg': []
}),
(5, {'label': 'Anaheim,+CA4099',
	  'received_msg': []
}),
(6, {'label': 'San+Jose,+CA4112',
	  'received_msg': []
}),
(7, {'label': 'San+Jose,+CA6742',
	  'received_msg': []
}),
(8, {'label': 'San+Jose,+CA4095',
	  'received_msg': []
}),
(9, {'label': 'San+Jose,+CA6405',
	  'received_msg': []
}),
(10, {'label': 'San+Jose,+CA4132',
	  'received_msg': []
}),
(11, {'label': 'Chicago,+IL4037',
	  'received_msg': []
}),
(12, {'label': 'Anaheim,+CA6490',
	  'received_msg': []
}),
(13, {'label': 'Manasquan,+NJ4086',
	  'received_msg': []
}),
(14, {'label': 'New+York,+NY4088',
	  'received_msg': []
}),
(15, {'label': 'Copenhagen4038',
	  'received_msg': []
}),
(16, {'label': 'Manasquan,+NJ4047',
	  'received_msg': []
}),
(17, {'label': 'Anaheim,+CA6564',
	  'received_msg': []
}),
(18, {'label': 'Anaheim,+CA4031',
	  'received_msg': []
}),
(19, {'label': 'Anaheim,+CA4073',
	  'received_msg': []
}),
(20, {'label': 'Anaheim,+CA6721',
	  'received_msg': []
}),
(21, {'label': 'Anaheim,+CA4100',
	  'received_msg': []
}),
(22, {'label': 'Dallas,+TX6566',
	  'received_msg': []
}),
(23, {'label': 'Dallas,+TX2635',
	  'received_msg': []
}),
(24, {'label': 'Dallas,+TX4015',
	  'received_msg': []
}),
(25, {'label': 'Dallas,+TX4080',
	  'received_msg': []
}),
(26, {'label': 'New+York,+NY4028',
	  'received_msg': []
}),
(27, {'label': 'Dallas,+TX4115',
	  'received_msg': []
}),
(28, {'label': 'Washington,+DC6456',
	  'received_msg': []
}),
(29, {'label': 'Washington,+DC6736',
	  'received_msg': []
}),
(30, {'label': 'Washington,+DC6543',
	  'received_msg': []
}),
(31, {'label': 'Washington,+DC6415',
	  'received_msg': []
}),
(32, {'label': 'Relay,+MD4093',
	  'received_msg': []
}),
(33, {'label': 'Washington,+DC6393',
	  'received_msg': []
}),
(34, {'label': 'Relay,+MD4054',
	  'received_msg': []
}),
(35, {'label': 'Tacoma,+WA6720',
	  'received_msg': []
}),
(36, {'label': 'Dallas,+TX6494',
	  'received_msg': []
}),
(37, {'label': 'Roachdale,+IN6712',
	  'received_msg': []
}),
(38, {'label': 'Roachdale,+IN4111',
	  'received_msg': []
}),
(39, {'label': 'Roachdale,+IN4056',
	  'received_msg': []
}),
(40, {'label': 'London4083',
	  'received_msg': []
}),
(41, {'label': 'London4044',
	  'received_msg': []
}),
(42, {'label': 'Brussels,+Belgium4033',
	  'received_msg': []
}),
(43, {'label': 'Dublin,+Ireland4078',
	  'received_msg': []
}),
(44, {'label': 'New+York,+NY4022',
	  'received_msg': []
}),
(45, {'label': 'London4084',
	  'received_msg': []
}),
(46, {'label': 'New+York,+NY4024',
	  'received_msg': []
}),
(47, {'label': 'Research+Triangle+Park,+NC4057',
	  'received_msg': []
}),
(48, {'label': 'Milan,+Italy4046',
	  'received_msg': []
}),
(49, {'label': 'Milan,+Italy4085',
	  'received_msg': []
}),
(50, {'label': 'Paris4090',
	  'received_msg': []
}),
(51, {'label': 'Pearl+Harbor,+HI4092',
	  'received_msg': []
}),
(52, {'label': 'Pearl+Harbor,+HI6400',
	  'received_msg': []
}),
(53, {'label': 'Pearl+Harbor,+HI4053',
	  'received_msg': []
}),
(54, {'label': 'Stockton,+CA4096',
	  'received_msg': []
}),
(55, {'label': 'Pearl+Harbor,+HI6550',
	  'received_msg': []
}),
(56, {'label': 'Research+Triangle+Park,+NC4058',
	  'received_msg': []
}),
(57, {'label': 'Atlanta,+GA4074',
	  'received_msg': []
}),
(58, {'label': 'Tacoma,+WA4114',
	  'received_msg': []
}),
(59, {'label': 'Tacoma,+WA6408',
	  'received_msg': []
}),
(60, {'label': 'Cheyenne,+WY4076',
	  'received_msg': []
}),
(61, {'label': 'Tacoma,+WA6555',
	  'received_msg': []
}),
(62, {'label': 'Tokyo4070',
	  'received_msg': []
}),
(63, {'label': 'Hamburg,+Germany4041',
	  'received_msg': []
}),
(64, {'label': 'Amsterdam4072',
	  'received_msg': []
}),
(65, {'label': 'Hamburg,+Germany4081',
	  'received_msg': []
}),
(66, {'label': 'Munich,+Germany4087',
	  'received_msg': []
}),
(67, {'label': 'Atlanta,+GA6565',
	  'received_msg': []
}),
(68, {'label': 'Atlanta,+GA3957',
	  'received_msg': []
}),
(69, {'label': 'Atlanta,+GA4032',
	  'received_msg': []
}),
(70, {'label': 'Relay,+MD6551',
	  'received_msg': []
}),
(71, {'label': 'Denver,+Colorado5511',
	  'received_msg': []
}),
(72, {'label': 'Cheyenne,+WY4034',
	  'received_msg': []
}),
(73, {'label': 'Pennsauken,+NJ6624',
	  'received_msg': []
}),
(74, {'label': 'Pennsauken,+NJ4109',
	  'received_msg': []
}),
(75, {'label': 'Pennsauken,+NJ4052',
	  'received_msg': []
}),
(76, {'label': 'Pennsauken,+NJ4091',
	  'received_msg': []
}),
(77, {'label': 'Lees+Summit,+MO5512',
	  'received_msg': []
}),
(78, {'label': 'Kansas+City,+MO4105',
	  'received_msg': []
}),
(79, {'label': 'Kansas+City,+MO4106',
	  'received_msg': []
}),
(80, {'label': 'Cheyenne,+WY6746',
	  'received_msg': []
}),
(81, {'label': 'Kansas+City,+MO6544',
	  'received_msg': []
}),
(82, {'label': 'Rancho+Cordova,+CA5507',
	  'received_msg': []
}),
(83, {'label': 'Rancho+Cordova,+CA5514',
	  'received_msg': []
}),
(84, {'label': 'Stockton,+CA4113',
	  'received_msg': []
}),
(85, {'label': 'Stockton,+CA4065',
	  'received_msg': []
}),
(86, {'label': 'Relay,+MD6487',
	  'received_msg': []
}),
(87, {'label': 'Pennsauken,+NJ6486',
	  'received_msg': []
}),
(88, {'label': 'Dallas,+TX6641',
	  'received_msg': []
}),
(89, {'label': 'Chicago,+IL6593',
	  'received_msg': []
}),
(90, {'label': 'Anaheim,+CA6464',
	  'received_msg': []
}),
(91, {'label': 'Anaheim,+CA6570',
	  'received_msg': []
}),
(92, {'label': 'Anaheim,+CA6627',
	  'received_msg': []
}),
(93, {'label': 'Anaheim,+CA6539',
	  'received_msg': []
}),
(94, {'label': 'Anaheim,+CA6556',
	  'received_msg': []
}),
(95, {'label': 'Anaheim,+CA6744',
	  'received_msg': []
}),
(96, {'label': 'Anaheim,+CA6591',
	  'received_msg': []
}),
(97, {'label': 'Dallas,+TX4133',
	  'received_msg': []
}),
(98, {'label': 'Anaheim,+CA6584',
	  'received_msg': []
}),
(99, {'label': 'Dallas,+TX6587',
	  'received_msg': []
}),
(100, {'label': 'Anaheim,+CA6684',
	  'received_msg': []
}),
(101, {'label': 'Anaheim,+CA6502',
	  'received_msg': []
}),
(102, {'label': 'Anaheim,+CA6520',
	  'received_msg': []
}),
(103, {'label': 'Anaheim,+CA6512',
	  'received_msg': []
}),
(104, {'label': 'Anaheim,+CA6702',
	  'received_msg': []
}),
(105, {'label': 'Anaheim,+CA6453',
	  'received_msg': []
}),
(106, {'label': 'Anaheim,+CA6438',
	  'received_msg': []
}),
(107, {'label': 'Kansas+City,+MO6707',
	  'received_msg': []
}),
(108, {'label': 'Kansas+City,+MO4082',
	  'received_msg': []
}),
(109, {'label': 'Kansas+City,+MO4043',
	  'received_msg': []
}),
(110, {'label': 'Dallas,+TX6645',
	  'received_msg': []
}),
(111, {'label': 'Los+Angeles,+CA5502',
	  'received_msg': []
}),
(112, {'label': 'Anaheim,+CA6578',
	  'received_msg': []
}),
(113, {'label': 'Dallas,+TX6573',
	  'received_msg': []
}),
(114, {'label': 'Dallas,+TX6558',
	  'received_msg': []
}),
(115, {'label': 'Relay,+MD5801',
	  'received_msg': []
}),
(116, {'label': 'Washington,+DC6443',
	  'received_msg': []
}),
(117, {'label': 'Washington,+DC9643',
	  'received_msg': []
}),
(118, {'label': 'Washington,+DC6469',
	  'received_msg': []
}),
(119, {'label': 'Washington,+DC4139',
	  'received_msg': []
}),
(120, {'label': 'Washington,+DC4140',
	  'received_msg': []
}),
(121, {'label': 'Washington,+DC6748',
	  'received_msg': []
}),
(122, {'label': 'Washington,+DC4142',
	  'received_msg': []
}),
(123, {'label': 'Chicago,+IL6492',
	  'received_msg': []
}),
(124, {'label': 'Chicago,+IL1391',
	  'received_msg': []
}),
(125, {'label': 'Chicago,+IL4122',
	  'received_msg': []
}),
(126, {'label': 'Chicago,+IL4036',
	  'received_msg': []
}),
(127, {'label': 'Chicago,+IL1484',
	  'received_msg': []
}),
(128, {'label': 'Chicago,+IL4104',
	  'received_msg': []
}),
(129, {'label': 'Chicago,+IL6639',
	  'received_msg': []
}),
(130, {'label': 'Pennsauken,+NJ4117',
	  'received_msg': []
}),
(131, {'label': 'Roachdale,+IN6729',
	  'received_msg': []
}),
(132, {'label': 'Roachdale,+IN6676',
	  'received_msg': []
}),
(133, {'label': 'Roachdale,+IN6552',
	  'received_msg': []
}),
(134, {'label': 'Roachdale,+IN6697',
	  'received_msg': []
}),
(135, {'label': 'Roachdale,+IN6402',
	  'received_msg': []
}),
(136, {'label': 'Roachdale,+IN6636',
	  'received_msg': []
}),
(137, {'label': 'Atlanta,+GA4102',
	  'received_msg': []
}),
(138, {'label': 'Orlando,+FL4049',
	  'received_msg': []
}),
(139, {'label': 'Atlanta,+GA6735',
	  'received_msg': []
}),
(140, {'label': 'Atlanta,+GA6745',
	  'received_msg': []
}),
(141, {'label': 'Atlanta,+GA2344',
	  'received_msg': []
}),
(142, {'label': 'Atlanta,+GA6685',
	  'received_msg': []
}),
(143, {'label': 'Atlanta,+GA2338',
	  'received_msg': []
}),
(144, {'label': 'Atlanta,+GA6540',
	  'received_msg': []
}),
(145, {'label': 'Orlando,+FL4050',
	  'received_msg': []
}),
(146, {'label': 'Atlanta,+GA2347',
	  'received_msg': []
}),
(147, {'label': 'Relay,+MD4131',
	  'received_msg': []
}),
(148, {'label': 'Atlanta,+GA6439',
	  'received_msg': []
}),
(149, {'label': 'Atlanta,+GA6465',
	  'received_msg': []
}),
(150, {'label': 'Atlanta,+GA6481',
	  'received_msg': []
}),
(151, {'label': 'Atlanta,+GA6628',
	  'received_msg': []
}),
(152, {'label': 'New+York,+NY4048',
	  'received_msg': []
}),
(153, {'label': 'Orlando,+FL4108',
	  'received_msg': []
}),
(154, {'label': 'Tacoma,+WA6701',
	  'received_msg': []
}),
(155, {'label': 'Seattle,+WA4059',
	  'received_msg': []
}),
(156, {'label': 'Sydney,+Australia4067',
	  'received_msg': []
}),
(157, {'label': 'Seattle,+WA4060',
	  'received_msg': []
}),
(158, {'label': 'Chicago,+IL6724',
	  'received_msg': []
}),
(159, {'label': 'Chicago,+IL6643',
	  'received_msg': []
}),
(160, {'label': 'Chicago,+IL6572',
	  'received_msg': []
}),
(161, {'label': 'Chicago,+IL6654',
	  'received_msg': []
}),
(162, {'label': 'Chicago,+IL6468',
	  'received_msg': []
}),
(163, {'label': 'Chicago,+IL6648',
	  'received_msg': []
}),
(164, {'label': 'Chicago,+IL6747',
	  'received_msg': []
}),
(165, {'label': 'Chicago,+IL6586',
	  'received_msg': []
}),
(166, {'label': 'Chicago,+IL6595',
	  'received_msg': []
}),
(167, {'label': 'Chicago,+IL6669',
	  'received_msg': []
}),
(168, {'label': 'Springfield,+MA4023',
	  'received_msg': []
}),
(169, {'label': 'Chicago,+IL6414',
	  'received_msg': []
}),
(170, {'label': 'Chicago,+IL6441',
	  'received_msg': []
}),
(171, {'label': 'Chicago,+IL6603',
	  'received_msg': []
}),
(172, {'label': 'Chicago,+IL6611',
	  'received_msg': []
}),
(173, {'label': 'Chicago,+IL6531',
	  'received_msg': []
}),
(174, {'label': 'Chicago,+IL6621',
	  'received_msg': []
}),
(175, {'label': 'Orlando,+FL6459',
	  'received_msg': []
}),
(176, {'label': 'New+York,+NY6427',
	  'received_msg': []
}),
(177, {'label': 'New+York,+NY4107',
	  'received_msg': []
}),
(178, {'label': 'New+York,+NY4116',
	  'received_msg': []
}),
(179, {'label': 'New+York,+NY6496',
	  'received_msg': []
}),
(180, {'label': 'Seattle,+WA6476',
	  'received_msg': []
}),
(181, {'label': 'Seattle,+WA4019',
	  'received_msg': []
}),
(182, {'label': 'Relay,+MD4029',
	  'received_msg': []
}),
(183, {'label': 'Cheyenne,+WY6455',
	  'received_msg': []
}),
(184, {'label': 'Denver,+Colorado5501',
	  'received_msg': []
}),
(185, {'label': 'Cheyenne,+WY2439',
	  'received_msg': []
}),
(186, {'label': 'Cheyenne,+WY6723',
	  'received_msg': []
}),
(187, {'label': 'Cheyenne,+WY6629',
	  'received_msg': []
}),
(188, {'label': 'Cheyenne,+WY6388',
	  'received_msg': []
}),
(189, {'label': 'Cheyenne,+WY6413',
	  'received_msg': []
}),
(190, {'label': 'Cheyenne,+WY6542',
	  'received_msg': []
}),
(191, {'label': 'Dallas,+TX6726',
	  'received_msg': []
}),
(192, {'label': 'Dallas,+TX6580',
	  'received_msg': []
}),
(193, {'label': 'Brussels,+Belgium4075',
	  'received_msg': []
}),
(194, {'label': 'Chicago,+IL6644',
	  'received_msg': []
}),
(195, {'label': 'Stockton,+CA6452',
	  'received_msg': []
}),
(196, {'label': 'Stockton,+CA4064',
	  'received_msg': []
}),
(197, {'label': 'Pennsauken,+NJ4135',
	  'received_msg': []
}),
(198, {'label': 'Dallas,+TX6483',
	  'received_msg': []
}),
(199, {'label': 'Dallas,+TX6737',
	  'received_msg': []
}),
(200, {'label': 'Orlando,+FL4089',
	  'received_msg': []
}),
(201, {'label': 'Dallas,+TX6749',
	  'received_msg': []
}),
(202, {'label': 'Chicago,+IL4123',
	  'received_msg': []
}),
(203, {'label': 'Dallas,+TX6598',
	  'received_msg': []
}),
(204, {'label': 'Dallas,+TX6689',
	  'received_msg': []
}),
(205, {'label': 'Dallas,+TX1742',
	  'received_msg': []
}),
(206, {'label': 'Dallas,+TX6504',
	  'received_msg': []
}),
(207, {'label': 'Dallas,+TX3549',
	  'received_msg': []
}),
(208, {'label': 'Dallas,+TX6604',
	  'received_msg': []
}),
(209, {'label': 'Dallas,+TX6612',
	  'received_msg': []
}),
(210, {'label': 'Dallas,+TX6419',
	  'received_msg': []
}),
(211, {'label': 'Dallas,+TX6622',
	  'received_msg': []
}),
(212, {'label': 'Dallas,+TX6444',
	  'received_msg': []
}),
(213, {'label': 'Dallas,+TX6706',
	  'received_msg': []
}),
(214, {'label': 'Dallas,+TX6471',
	  'received_msg': []
}),
(215, {'label': 'Kansas+City,+MO6472',
	  'received_msg': []
}),
(216, {'label': 'Kansas+City,+MO6458',
	  'received_msg': []
}),
(217, {'label': 'Kansas+City,+MO6395',
	  'received_msg': []
}),
(218, {'label': 'Kansas+City,+MO6422',
	  'received_msg': []
}),
(219, {'label': 'Kansas+City,+MO6690',
	  'received_msg': []
}),
(220, {'label': 'Chicago,+IL6652',
	  'received_msg': []
}),
(221, {'label': 'Dallas,+TX6658',
	  'received_msg': []
}),
(222, {'label': 'Springfield,+MA4020',
	  'received_msg': []
}),
(223, {'label': 'New+York,+NY4124',
	  'received_msg': []
}),
(224, {'label': 'Pennsauken,+NJ4125',
	  'received_msg': []
}),
(225, {'label': 'Pennsauken,+NJ4126',
	  'received_msg': []
}),
(226, {'label': 'Roachdale,+IN6677',
	  'received_msg': []
}),
(227, {'label': 'Relay,+MD6576',
	  'received_msg': []
}),
(228, {'label': 'Relay,+MD4127',
	  'received_msg': []
}),
(229, {'label': 'Seattle,+WA6450',
	  'received_msg': []
}),
(230, {'label': 'Pennsauken,+NJ6647',
	  'received_msg': []
}),
(231, {'label': 'Stockton,+CA6602',
	  'received_msg': []
}),
(232, {'label': 'Pennsauken,+NJ6516',
	  'received_msg': []
}),
(233, {'label': 'Pennsauken,+NJ6614',
	  'received_msg': []
}),
(234, {'label': 'Pennsauken,+NJ6525',
	  'received_msg': []
}),
(235, {'label': 'Pennsauken,+NJ6517',
	  'received_msg': []
}),
(236, {'label': 'Pennsauken,+NJ6448',
	  'received_msg': []
}),
(237, {'label': 'Pennsauken,+NJ6728',
	  'received_msg': []
}),
(238, {'label': 'Pennsauken,+NJ6754',
	  'received_msg': []
}),
(239, {'label': 'Dallas,+TX6663',
	  'received_msg': []
}),
(240, {'label': 'Chicago,+IL6651',
	  'received_msg': []
}),
(241, {'label': 'Amsterdam4030',
	  'received_msg': []
}),
(242, {'label': 'Stockton,+CA6609',
	  'received_msg': []
}),
(243, {'label': 'Stockton,+CA6463',
	  'received_msg': []
}),
(244, {'label': 'San+Jose,+CA6477',
	  'received_msg': []
}),
(245, {'label': 'Kansas+City,+MO6750',
	  'received_msg': []
}),
(246, {'label': 'Lees+Summit,+MO5504',
	  'received_msg': []
}),
(247, {'label': 'Hong+Kong4042',
	  'received_msg': []
}),
(248, {'label': 'Hong+Kong6421',
	  'received_msg': []
}),
(249, {'label': 'Tokyo4069',
	  'received_msg': []
}),
(250, {'label': 'Relay,+MD4136',
	  'received_msg': []
}),
(251, {'label': 'Relay,+MD6461',
	  'received_msg': []
}),
(252, {'label': 'Relay,+MD6518',
	  'received_msg': []
}),
(253, {'label': 'Relay,+MD4138',
	  'received_msg': []
}),
(254, {'label': 'Relay,+MD6431',
	  'received_msg': []
}),
(255, {'label': 'Relay,+MD6696',
	  'received_msg': []
}),
(256, {'label': 'Relay,+MD6675',
	  'received_msg': []
}),
(257, {'label': 'Relay,+MD4118',
	  'received_msg': []
}),
(258, {'label': 'Relay,+MD6449',
	  'received_msg': []
}),
(259, {'label': 'New+York,+NY6446',
	  'received_msg': []
}),
(260, {'label': 'Sydney,+Australia6437',
	  'received_msg': []
}),
(261, {'label': 'Sydney,+Australia4068',
	  'received_msg': []
}),
(262, {'label': 'Atlanta,+GA6530',
	  'received_msg': []
}),
(263, {'label': 'Springfield,+MA4025',
	  'received_msg': []
}),
(264, {'label': 'Stockton,+CA6619',
	  'received_msg': []
}),
(265, {'label': 'Stockton,+CA6479',
	  'received_msg': []
}),
(266, {'label': 'Frankfurt4040',
	  'received_msg': []
}),
(267, {'label': 'Copenhagen4077',
	  'received_msg': []
}),
(268, {'label': 'New+York,+NY6524',
	  'received_msg': []
}),
(269, {'label': 'New+York,+NY4129',
	  'received_msg': []
}),
(270, {'label': 'Reston,+VA5496',
	  'received_msg': []
}),
(271, {'label': 'Ashburn,+VA10163',
	  'received_msg': []
}),
(272, {'label': 'Pennsauken,+NJ6399',
	  'received_msg': []
}),
(273, {'label': 'Dallas,+TX6683',
	  'received_msg': []
}),
(274, {'label': 'Anaheim,+CA6610',
	  'received_msg': []
}),
(275, {'label': 'New+York,+NY6605',
	  'received_msg': []
}),
(276, {'label': 'New+York,+NY6606',
	  'received_msg': []
}),
(277, {'label': 'New+York,+NY6532',
	  'received_msg': []
}),
(278, {'label': 'New+York,+NY6397',
	  'received_msg': []
}),
(279, {'label': 'Ashburn,+VA10162',
	  'received_msg': []
}),
(280, {'label': 'Paris4051',
	  'received_msg': []
}),
(281, {'label': 'Frankfurt4079',
	  'received_msg': []
}),
(282, {'label': 'Ashburn,+VA10161',
	  'received_msg': []
}),
(283, {'label': 'Stockton,+CA6563',
	  'received_msg': []
}),
(284, {'label': 'Richardson,+TX5500',
	  'received_msg': []
}),
(285, {'label': 'Stockton,+CA6569',
	  'received_msg': []
}),
(286, {'label': 'Orlando,+FL6429',
	  'received_msg': []
}),
(287, {'label': 'Orlando,+FL6693',
	  'received_msg': []
}),
(288, {'label': 'Seattle,+WA6432',
	  'received_msg': []
}),
(289, {'label': 'Stockton,+CA6719',
	  'received_msg': []
}),
(290, {'label': 'Lees+Summit,+MO5503',
	  'received_msg': []
}),
(291, {'label': 'Lees+Summit,+MO5505',
	  'received_msg': []
}),
(292, {'label': 'Stockton,+CA6577',
	  'received_msg': []
}),
(293, {'label': 'Stockholm,+Sweden4066',
	  'received_msg': []
}),
(294, {'label': 'New+York,+NY4017',
	  'received_msg': []
}),
(295, {'label': 'London4045',
	  'received_msg': []
}),
(296, {'label': 'New+York,+NY4134',
	  'received_msg': []
}),
(297, {'label': 'New+York,+NY6559',
	  'received_msg': []
}),
(298, {'label': 'Stockton,+CA6407',
	  'received_msg': []
}),
(299, {'label': 'Stockton,+CA6590',
	  'received_msg': []
}),
(300, {'label': 'Stockton,+CA3402',
	  'received_msg': []
}),
(301, {'label': 'Stockton,+CA6583',
	  'received_msg': []
}),
(302, {'label': 'Stockton,+CA6758',
	  'received_msg': []
}),
(303, {'label': 'Boston5499',
	  'received_msg': []
}),
(304, {'label': 'Springfield,+MA6406',
	  'received_msg': []
}),
(305, {'label': 'New+York,+NY4137',
	  'received_msg': []
}),
(306, {'label': 'Boston5509',
	  'received_msg': []
}),
(307, {'label': 'Stockholm,+Sweden4097',
	  'received_msg': []
}),
(308, {'label': 'Reston,+VA5497',
	  'received_msg': []
}),
(309, {'label': 'Tokyo4071',
	  'received_msg': []
}),
(310, {'label': 'Singapore4094',
	  'received_msg': []
}),
(311, {'label': 'New+York,+NY6751',
	  'received_msg': []
}),
(312, {'label': 'New+York,+NY6752',
	  'received_msg': []
}),
(313, {'label': 'Santa+Clara,+CA5508',
	  'received_msg': []
}),
(314, {'label': 'Dublin,+Ireland4039',
	  'received_msg': []
}),
])
network.add_edges_from([
(0, 1, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_0'
}),
(0, 2, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1'
}),
(0, 3, {
	'weight': 650,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_2'
}),
(0, 4, {
	'weight': 800,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_3'
}),
(0, 5, {
	'weight': 850,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_4'
}),
(0, 6, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_5'
}),
(0, 7, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_6'
}),
(0, 8, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_7'
}),
(0, 9, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_8'
}),
(0, 10, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_9'
}),
(0, 11, {
	'weight': 900,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_10'
}),
(12, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_11'
}),
(12, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_12'
}),
(13, 14, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_13'
}),
(13, 15, {
	'weight': 300,
	'bw': 10000000,
	'delay': 33,
	'label': 'Link_14'
}),
(13, 16, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_15'
}),
(13, 4, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_16'
}),
(17, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_17'
}),
(17, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_18'
}),
(17, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_19'
}),
(17, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_20'
}),
(17, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_21'
}),
(17, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_22'
}),
(22, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_23'
}),
(22, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_24'
}),
(22, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_25'
}),
(22, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_26'
}),
(22, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_27'
}),
(28, 29, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_28'
}),
(28, 30, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_29'
}),
(28, 31, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_30'
}),
(28, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_31'
}),
(28, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_32'
}),
(28, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_33'
}),
(28, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_34'
}),
(35, 3, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_35'
}),
(36, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_36'
}),
(36, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_37'
}),
(36, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_38'
}),
(36, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_39'
}),
(36, 27, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_40'
}),
(37, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_41'
}),
(37, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_42'
}),
(40, 41, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_43'
}),
(40, 42, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_44'
}),
(40, 16, {
	'weight': 250,
	'bw': 10000000,
	'delay': 30,
	'label': 'Link_45'
}),
(40, 43, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_46'
}),
(40, 44, {
	'weight': 950,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_47'
}),
(45, 46, {
	'weight': 900,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_48'
}),
(45, 42, {
	'weight': 800,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_49'
}),
(45, 16, {
	'weight': 450,
	'bw': 10000000,
	'delay': 30,
	'label': 'Link_50'
}),
(45, 44, {
	'weight': 750,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_51'
}),
(47, 34, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_52'
}),
(48, 49, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_53'
}),
(48, 50, {
	'weight': 200,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_54'
}),
(51, 5, {
	'weight': 700,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_55'
}),
(51, 52, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_56'
}),
(51, 53, {
	'weight': 950,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_57'
}),
(51, 54, {
	'weight': 850,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_58'
}),
(51, 55, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_59'
}),
(51, 21, {
	'weight': 1600,
	'bw': 2400000,
	'delay': 22,
	'label': 'Link_60'
}),
(56, 57, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_61'
}),
(58, 8, {
	'weight': 650,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_62'
}),
(58, 59, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_63'
}),
(58, 3, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_64'
}),
(58, 60, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_65'
}),
(58, 61, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_66'
}),
(58, 62, {
	'weight': 600,
	'bw': 10000000,
	'delay': 40,
	'label': 'Link_67'
}),
(63, 15, {
	'weight': 450,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_68'
}),
(63, 64, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_69'
}),
(63, 65, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_70'
}),
(63, 66, {
	'weight': 100,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_71'
}),
(67, 68, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_72'
}),
(67, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_73'
}),
(70, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_74'
}),
(70, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_75'
}),
(70, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_76'
}),
(71, 72, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_77'
}),
(73, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_78'
}),
(73, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_79'
}),
(73, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_80'
}),
(77, 78, {
	'weight': 350,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_81'
}),
(77, 79, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_82'
}),
(80, 81, {
	'weight': 100,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_83'
}),
(82, 83, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_84'
}),
(82, 84, {
	'weight': 250,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_85'
}),
(82, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_86'
}),
(86, 4, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_87'
}),
(87, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_88'
}),
(87, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_89'
}),
(87, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_90'
}),
(88, 68, {
	'weight': 750,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_91'
}),
(88, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_92'
}),
(88, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_93'
}),
(88, 25, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_94'
}),
(88, 89, {
	'weight': 650,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_95'
}),
(88, 26, {
	'weight': 400,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_96'
}),
(88, 27, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_97'
}),
(21, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_98'
}),
(21, 2, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_99'
}),
(21, 90, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_100'
}),
(21, 91, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_101'
}),
(21, 92, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_102'
}),
(21, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_103'
}),
(21, 93, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_104'
}),
(21, 53, {
	'weight': 750,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_105'
}),
(21, 94, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_106'
}),
(21, 17, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_107'
}),
(21, 95, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_108'
}),
(21, 96, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_109'
}),
(21, 97, {
	'weight': 200,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_110'
}),
(21, 98, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_111'
}),
(21, 51, {
	'weight': 1600,
	'bw': 2400000,
	'delay': 22,
	'label': 'Link_112'
}),
(21, 99, {
	'weight': 600,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_113'
}),
(21, 100, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_114'
}),
(21, 25, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_115'
}),
(21, 19, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_116'
}),
(21, 101, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_117'
}),
(21, 102, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_118'
}),
(21, 103, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_119'
}),
(21, 5, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_120'
}),
(21, 6, {
	'weight': 550,
	'bw': 2400000,
	'delay': 4,
	'label': 'Link_121'
}),
(21, 104, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_122'
}),
(21, 105, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_123'
}),
(21, 20, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_124'
}),
(21, 106, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_125'
}),
(1, 0, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_126'
}),
(1, 90, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_127'
}),
(1, 92, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_128'
}),
(1, 12, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_129'
}),
(1, 53, {
	'weight': 750,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_130'
}),
(1, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_131'
}),
(1, 93, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_132'
}),
(1, 17, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_133'
}),
(1, 94, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_134'
}),
(1, 95, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_135'
}),
(1, 96, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_136'
}),
(1, 98, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_137'
}),
(1, 100, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_138'
}),
(1, 25, {
	'weight': 700,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_139'
}),
(1, 19, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_140'
}),
(1, 23, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_141'
}),
(1, 101, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_142'
}),
(1, 102, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_143'
}),
(1, 103, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_144'
}),
(1, 5, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_145'
}),
(1, 104, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_146'
}),
(1, 20, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_147'
}),
(1, 105, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_148'
}),
(1, 106, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_149'
}),
(1, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_150'
}),
(107, 108, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_151'
}),
(107, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_152'
}),
(107, 78, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_153'
}),
(107, 79, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_154'
}),
(91, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_155'
}),
(91, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_156'
}),
(110, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_157'
}),
(110, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_158'
}),
(110, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_159'
}),
(110, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_160'
}),
(110, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_161'
}),
(18, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_162'
}),
(18, 90, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_163'
}),
(18, 91, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_164'
}),
(18, 92, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_165'
}),
(18, 93, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_166'
}),
(18, 94, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_167'
}),
(18, 17, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_168'
}),
(18, 26, {
	'weight': 600,
	'bw': 2400000,
	'delay': 21,
	'label': 'Link_169'
}),
(18, 27, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_170'
}),
(18, 95, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_171'
}),
(18, 111, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_172'
}),
(18, 112, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_173'
}),
(18, 100, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_174'
}),
(18, 101, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_175'
}),
(18, 103, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_176'
}),
(18, 102, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_177'
}),
(18, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_178'
}),
(18, 6, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_179'
}),
(18, 104, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_180'
}),
(18, 105, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_181'
}),
(18, 20, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_182'
}),
(18, 106, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_183'
}),
(18, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_184'
}),
(113, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_185'
}),
(113, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_186'
}),
(113, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_187'
}),
(113, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_188'
}),
(113, 114, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_189'
}),
(113, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_190'
}),
(113, 115, {
	'weight': 1550,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_191'
}),
(33, 116, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_192'
}),
(33, 117, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_193'
}),
(33, 118, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_194'
}),
(33, 119, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_195'
}),
(33, 120, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_196'
}),
(33, 28, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_197'
}),
(33, 121, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_198'
}),
(33, 122, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_199'
}),
(123, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_200'
}),
(123, 125, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_201'
}),
(123, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_202'
}),
(123, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_203'
}),
(123, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_204'
}),
(123, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_205'
}),
(129, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_206'
}),
(129, 125, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_207'
}),
(129, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_208'
}),
(129, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_209'
}),
(129, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_210'
}),
(129, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_211'
}),
(112, 18, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_212'
}),
(118, 31, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_213'
}),
(118, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_214'
}),
(118, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_215'
}),
(118, 33, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_216'
}),
(118, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_217'
}),
(38, 130, {
	'weight': 900,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_218'
}),
(38, 131, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_219'
}),
(38, 132, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_220'
}),
(38, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_221'
}),
(38, 128, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_222'
}),
(38, 37, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_223'
}),
(38, 133, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_224'
}),
(38, 134, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_225'
}),
(38, 135, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_226'
}),
(38, 136, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_227'
}),
(38, 126, {
	'weight': 950,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_228'
}),
(137, 138, {
	'weight': 300,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_229'
}),
(137, 139, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_230'
}),
(137, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_231'
}),
(137, 140, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_232'
}),
(137, 141, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_233'
}),
(137, 142, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_234'
}),
(137, 143, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_235'
}),
(137, 144, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_236'
}),
(137, 145, {
	'weight': 350,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_237'
}),
(137, 146, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_238'
}),
(137, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_239'
}),
(137, 147, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_240'
}),
(137, 148, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_241'
}),
(137, 149, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_242'
}),
(137, 150, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_243'
}),
(137, 151, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_244'
}),
(131, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_245'
}),
(131, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_246'
}),
(69, 32, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_247'
}),
(69, 144, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_248'
}),
(69, 152, {
	'weight': 650,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_249'
}),
(69, 11, {
	'weight': 800,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_250'
}),
(69, 150, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_251'
}),
(69, 149, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_252'
}),
(69, 137, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_253'
}),
(69, 151, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_254'
}),
(69, 67, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_255'
}),
(69, 23, {
	'weight': 550,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_256'
}),
(69, 139, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_257'
}),
(69, 68, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_258'
}),
(69, 140, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_259'
}),
(69, 141, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_260'
}),
(69, 142, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_261'
}),
(69, 143, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_262'
}),
(69, 146, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_263'
}),
(69, 153, {
	'weight': 200,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_264'
}),
(69, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_265'
}),
(3, 0, {
	'weight': 650,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_266'
}),
(3, 59, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_267'
}),
(3, 60, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_268'
}),
(3, 154, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_269'
}),
(3, 155, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_270'
}),
(3, 35, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_271'
}),
(3, 156, {
	'weight': 650,
	'bw': 10000000,
	'delay': 64,
	'label': 'Link_272'
}),
(3, 72, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_273'
}),
(3, 61, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_274'
}),
(3, 157, {
	'weight': 300,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_275'
}),
(3, 58, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_276'
}),
(3, 62, {
	'weight': 800,
	'bw': 10000000,
	'delay': 40,
	'label': 'Link_277'
}),
(127, 60, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_278'
}),
(127, 158, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_279'
}),
(127, 159, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_280'
}),
(127, 160, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_281'
}),
(127, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_282'
}),
(127, 123, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_283'
}),
(127, 161, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_284'
}),
(127, 162, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_285'
}),
(127, 129, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_286'
}),
(127, 125, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_287'
}),
(127, 163, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_288'
}),
(127, 164, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_289'
}),
(127, 89, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_290'
}),
(127, 25, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_291'
}),
(127, 165, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_292'
}),
(127, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_293'
}),
(127, 166, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_294'
}),
(127, 167, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_295'
}),
(127, 14, {
	'weight': 850,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_296'
}),
(127, 124, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_297'
}),
(127, 168, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_298'
}),
(127, 72, {
	'weight': 800,
	'bw': 2400000,
	'delay': 9,
	'label': 'Link_299'
}),
(127, 169, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_300'
}),
(127, 57, {
	'weight': 800,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_301'
}),
(127, 170, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_302'
}),
(127, 171, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_303'
}),
(127, 172, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_304'
}),
(127, 173, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_305'
}),
(127, 174, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_306'
}),
(175, 138, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_307'
}),
(175, 145, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_308'
}),
(176, 14, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_309'
}),
(176, 152, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_310'
}),
(176, 177, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_311'
}),
(176, 178, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_312'
}),
(176, 179, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_313'
}),
(83, 82, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_314'
}),
(83, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_315'
}),
(180, 181, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_316'
}),
(20, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_317'
}),
(20, 90, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_318'
}),
(20, 92, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_319'
}),
(20, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_320'
}),
(20, 93, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_321'
}),
(20, 94, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_322'
}),
(20, 17, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_323'
}),
(20, 95, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_324'
}),
(20, 100, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_325'
}),
(20, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_326'
}),
(20, 101, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_327'
}),
(20, 102, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_328'
}),
(20, 103, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_329'
}),
(20, 104, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_330'
}),
(20, 105, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_331'
}),
(20, 106, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_332'
}),
(20, 21, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_333'
}),
(182, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_334'
}),
(182, 34, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_335'
}),
(60, 183, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_336'
}),
(60, 184, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_337'
}),
(60, 185, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_338'
}),
(60, 186, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_339'
}),
(60, 3, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_340'
}),
(60, 127, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_341'
}),
(60, 187, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_342'
}),
(60, 188, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_343'
}),
(60, 189, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_344'
}),
(60, 72, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_345'
}),
(60, 25, {
	'weight': 1350,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_346'
}),
(60, 58, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_347'
}),
(60, 190, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_348'
}),
(191, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_349'
}),
(191, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_350'
}),
(191, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_351'
}),
(191, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_352'
}),
(191, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_353'
}),
(192, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_354'
}),
(192, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_355'
}),
(192, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_356'
}),
(192, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_357'
}),
(192, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_358'
}),
(30, 116, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_359'
}),
(30, 119, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_360'
}),
(30, 120, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_361'
}),
(30, 28, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_362'
}),
(30, 122, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_363'
}),
(30, 121, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_364'
}),
(42, 41, {
	'weight': 500,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_365'
}),
(42, 45, {
	'weight': 800,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_366'
}),
(42, 193, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_367'
}),
(42, 40, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_368'
}),
(159, 139, {
	'weight': 1300,
	'bw': 2400000,
	'delay': 6,
	'label': 'Link_369'
}),
(159, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_370'
}),
(159, 194, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_371'
}),
(195, 196, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_372'
}),
(195, 84, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_373'
}),
(195, 85, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_374'
}),
(195, 54, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_375'
}),
(27, 197, {
	'weight': 900,
	'bw': 10000000,
	'delay': 12,
	'label': 'Link_376'
}),
(27, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_377'
}),
(27, 192, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_378'
}),
(27, 191, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_379'
}),
(27, 110, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_380'
}),
(27, 198, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_381'
}),
(27, 18, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_382'
}),
(27, 113, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_383'
}),
(27, 22, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_384'
}),
(27, 78, {
	'weight': 450,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_385'
}),
(27, 36, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_386'
}),
(27, 199, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_387'
}),
(27, 200, {
	'weight': 650,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_388'
}),
(27, 99, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_389'
}),
(27, 201, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_390'
}),
(27, 202, {
	'weight': 100,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_391'
}),
(27, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_392'
}),
(27, 203, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_393'
}),
(27, 204, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_394'
}),
(27, 205, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_395'
}),
(27, 124, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_396'
}),
(27, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_397'
}),
(27, 206, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_398'
}),
(27, 207, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_399'
}),
(27, 208, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_400'
}),
(27, 209, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_401'
}),
(27, 210, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_402'
}),
(27, 211, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_403'
}),
(27, 212, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_404'
}),
(27, 88, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_405'
}),
(27, 213, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_406'
}),
(27, 214, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_407'
}),
(194, 11, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_408'
}),
(194, 159, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_409'
}),
(78, 108, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_410'
}),
(78, 130, {
	'weight': 1250,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_411'
}),
(78, 23, {
	'weight': 550,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_412'
}),
(78, 81, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_413'
}),
(78, 215, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_414'
}),
(78, 107, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_415'
}),
(78, 216, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_416'
}),
(78, 26, {
	'weight': 650,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_417'
}),
(78, 27, {
	'weight': 450,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_418'
}),
(78, 217, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_419'
}),
(78, 218, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_420'
}),
(78, 77, {
	'weight': 350,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_421'
}),
(78, 109, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_422'
}),
(78, 219, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_423'
}),
(160, 127, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_424'
}),
(160, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_425'
}),
(79, 108, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_426'
}),
(79, 130, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_427'
}),
(79, 23, {
	'weight': 500,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_428'
}),
(79, 81, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_429'
}),
(79, 215, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_430'
}),
(79, 107, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_431'
}),
(79, 216, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_432'
}),
(79, 217, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_433'
}),
(79, 77, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_434'
}),
(79, 218, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_435'
}),
(79, 109, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_436'
}),
(79, 219, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_437'
}),
(128, 178, {
	'weight': 1150,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_438'
}),
(128, 155, {
	'weight': 350,
	'bw': 10000000,
	'delay': 15,
	'label': 'Link_439'
}),
(128, 158, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_440'
}),
(128, 220, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_441'
}),
(128, 152, {
	'weight': 850,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_442'
}),
(128, 123, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_443'
}),
(128, 162, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_444'
}),
(128, 109, {
	'weight': 600,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_445'
}),
(128, 129, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_446'
}),
(128, 125, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_447'
}),
(128, 38, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_448'
}),
(128, 164, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_449'
}),
(128, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_450'
}),
(128, 89, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_451'
}),
(128, 25, {
	'weight': 750,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_452'
}),
(128, 165, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_453'
}),
(128, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_454'
}),
(128, 166, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_455'
}),
(128, 167, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_456'
}),
(128, 124, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_457'
}),
(128, 23, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_458'
}),
(128, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_459'
}),
(128, 72, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_460'
}),
(128, 169, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_461'
}),
(128, 170, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_462'
}),
(128, 171, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_463'
}),
(128, 172, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_464'
}),
(128, 173, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_465'
}),
(128, 174, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_466'
}),
(221, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_467'
}),
(221, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_468'
}),
(98, 5, {
	'weight': 1000,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_469'
}),
(98, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_470'
}),
(98, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_471'
}),
(163, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_472'
}),
(163, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_473'
}),
(99, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_474'
}),
(99, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_475'
}),
(99, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_476'
}),
(99, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_477'
}),
(99, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_478'
}),
(99, 21, {
	'weight': 600,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_479'
}),
(9, 0, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_480'
}),
(9, 8, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_481'
}),
(126, 158, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_482'
}),
(126, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_483'
}),
(126, 123, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_484'
}),
(126, 162, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_485'
}),
(126, 129, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_486'
}),
(126, 125, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_487'
}),
(126, 38, {
	'weight': 950,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_488'
}),
(126, 84, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_489'
}),
(126, 89, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_490'
}),
(126, 164, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_491'
}),
(126, 25, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_492'
}),
(126, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_493'
}),
(126, 165, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_494'
}),
(126, 166, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_495'
}),
(126, 167, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_496'
}),
(126, 124, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_497'
}),
(126, 222, {
	'weight': 600,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_498'
}),
(126, 85, {
	'weight': 1100,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_499'
}),
(126, 169, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_500'
}),
(126, 172, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_501'
}),
(126, 170, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_502'
}),
(126, 171, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_503'
}),
(126, 173, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_504'
}),
(126, 174, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_505'
}),
(11, 0, {
	'weight': 900,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_506'
}),
(11, 223, {
	'weight': 750,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_507'
}),
(11, 158, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_508'
}),
(11, 194, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_509'
}),
(11, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_510'
}),
(11, 160, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_511'
}),
(11, 161, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_512'
}),
(11, 123, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_513'
}),
(11, 162, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_514'
}),
(11, 109, {
	'weight': 600,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_515'
}),
(11, 129, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_516'
}),
(11, 125, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_517'
}),
(11, 163, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_518'
}),
(11, 164, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_519'
}),
(11, 89, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_520'
}),
(11, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_521'
}),
(11, 25, {
	'weight': 750,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_522'
}),
(11, 165, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_523'
}),
(11, 166, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_524'
}),
(11, 167, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_525'
}),
(11, 69, {
	'weight': 800,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_526'
}),
(11, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_527'
}),
(11, 39, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_528'
}),
(11, 72, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_529'
}),
(11, 169, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_530'
}),
(11, 171, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_531'
}),
(11, 170, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_532'
}),
(11, 172, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_533'
}),
(11, 173, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_534'
}),
(11, 174, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_535'
}),
(39, 224, {
	'weight': 850,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_536'
}),
(39, 131, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_537'
}),
(39, 225, {
	'weight': 750,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_538'
}),
(39, 226, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_539'
}),
(39, 37, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_540'
}),
(39, 134, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_541'
}),
(39, 133, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_542'
}),
(39, 135, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_543'
}),
(39, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_544'
}),
(39, 136, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_545'
}),
(39, 11, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_546'
}),
(227, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_547'
}),
(227, 228, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_548'
}),
(181, 180, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_549'
}),
(181, 155, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_550'
}),
(181, 157, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_551'
}),
(181, 229, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_552'
}),
(230, 197, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_553'
}),
(231, 196, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_554'
}),
(231, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_555'
}),
(74, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_556'
}),
(74, 130, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_557'
}),
(74, 177, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_558'
}),
(74, 24, {
	'weight': 900,
	'bw': 10000000,
	'delay': 12,
	'label': 'Link_559'
}),
(74, 197, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_560'
}),
(74, 178, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_561'
}),
(74, 76, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_562'
}),
(74, 232, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_563'
}),
(74, 233, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_564'
}),
(74, 234, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_565'
}),
(74, 235, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_566'
}),
(74, 73, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_567'
}),
(74, 236, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_568'
}),
(74, 54, {
	'weight': 650,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_569'
}),
(74, 237, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_570'
}),
(74, 87, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_571'
}),
(74, 238, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_572'
}),
(158, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_573'
}),
(158, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_574'
}),
(158, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_575'
}),
(158, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_576'
}),
(158, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_577'
}),
(239, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_578'
}),
(239, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_579'
}),
(240, 125, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_580'
}),
(64, 241, {
	'weight': 600,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_581'
}),
(64, 63, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_582'
}),
(199, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_583'
}),
(199, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_584'
}),
(199, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_585'
}),
(199, 26, {
	'weight': 500,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_586'
}),
(199, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_587'
}),
(220, 128, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_588'
}),
(96, 1, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_589'
}),
(96, 5, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_590'
}),
(96, 21, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_591'
}),
(161, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_592'
}),
(161, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_593'
}),
(242, 84, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_594'
}),
(242, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_595'
}),
(242, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_596'
}),
(243, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_597'
}),
(243, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_598'
}),
(243, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_599'
}),
(243, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_600'
}),
(8, 0, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_601'
}),
(8, 2, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_602'
}),
(8, 85, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_603'
}),
(8, 6, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_604'
}),
(8, 244, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_605'
}),
(8, 9, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_606'
}),
(8, 84, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_607'
}),
(8, 19, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_608'
}),
(8, 58, {
	'weight': 650,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_609'
}),
(109, 108, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_610'
}),
(109, 81, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_611'
}),
(109, 24, {
	'weight': 550,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_612'
}),
(109, 215, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_613'
}),
(109, 107, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_614'
}),
(109, 216, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_615'
}),
(109, 245, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_616'
}),
(109, 217, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_617'
}),
(109, 78, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_618'
}),
(109, 79, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_619'
}),
(109, 128, {
	'weight': 600,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_620'
}),
(109, 246, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_621'
}),
(109, 219, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_622'
}),
(109, 157, {
	'weight': 650,
	'bw': 10000000,
	'delay': 14,
	'label': 'Link_623'
}),
(109, 11, {
	'weight': 600,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_624'
}),
(203, 23, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_625'
}),
(203, 139, {
	'weight': 700,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_626'
}),
(203, 24, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_627'
}),
(203, 25, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_628'
}),
(203, 89, {
	'weight': 600,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_629'
}),
(203, 26, {
	'weight': 650,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_630'
}),
(203, 216, {
	'weight': 700,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_631'
}),
(203, 27, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_632'
}),
(165, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_633'
}),
(165, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_634'
}),
(165, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_635'
}),
(165, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_636'
}),
(165, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_637'
}),
(139, 69, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_638'
}),
(139, 57, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_639'
}),
(139, 159, {
	'weight': 1300,
	'bw': 2400000,
	'delay': 6,
	'label': 'Link_640'
}),
(139, 203, {
	'weight': 700,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_641'
}),
(139, 137, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_642'
}),
(247, 248, {
	'weight': 1250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_643'
}),
(247, 249, {
	'weight': 450,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_644'
}),
(247, 62, {
	'weight': 200,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_645'
}),
(132, 38, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_646'
}),
(226, 39, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_647'
}),
(4, 152, {
	'weight': 550,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_648'
}),
(4, 116, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_649'
}),
(4, 250, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_650'
}),
(4, 0, {
	'weight': 800,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_651'
}),
(4, 117, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_652'
}),
(4, 118, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_653'
}),
(4, 251, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_654'
}),
(4, 252, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_655'
}),
(4, 253, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_656'
}),
(4, 57, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_657'
}),
(4, 147, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_658'
}),
(4, 178, {
	'weight': 750,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_659'
}),
(4, 70, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_660'
}),
(4, 119, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_661'
}),
(4, 13, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_662'
}),
(4, 254, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_663'
}),
(4, 120, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_664'
}),
(4, 86, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_665'
}),
(4, 255, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_666'
}),
(4, 28, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_667'
}),
(4, 256, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_668'
}),
(4, 257, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_669'
}),
(4, 182, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_670'
}),
(4, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_671'
}),
(4, 258, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_672'
}),
(4, 115, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_673'
}),
(4, 121, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_674'
}),
(259, 14, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_675'
}),
(259, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_676'
}),
(259, 177, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_677'
}),
(259, 178, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_678'
}),
(259, 179, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_679'
}),
(237, 75, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_680'
}),
(237, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_681'
}),
(237, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_682'
}),
(257, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_683'
}),
(257, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_684'
}),
(257, 76, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_685'
}),
(257, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_686'
}),
(257, 228, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_687'
}),
(43, 40, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_688'
}),
(130, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_689'
}),
(130, 225, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_690'
}),
(130, 197, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_691'
}),
(130, 38, {
	'weight': 900,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_692'
}),
(130, 78, {
	'weight': 1250,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_693'
}),
(130, 79, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_694'
}),
(130, 76, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_695'
}),
(260, 156, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_696'
}),
(260, 261, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_697'
}),
(95, 1, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_698'
}),
(95, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_699'
}),
(95, 18, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_700'
}),
(95, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_701'
}),
(95, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_702'
}),
(95, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_703'
}),
(111, 18, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_704'
}),
(189, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_705'
}),
(189, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_706'
}),
(189, 262, {
	'weight': 100,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_707'
}),
(97, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_708'
}),
(97, 23, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_709'
}),
(97, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_710'
}),
(125, 124, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_711'
}),
(125, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_712'
}),
(125, 240, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_713'
}),
(125, 263, {
	'weight': 500,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_714'
}),
(125, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_715'
}),
(125, 123, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_716'
}),
(125, 129, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_717'
}),
(125, 169, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_718'
}),
(125, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_719'
}),
(125, 172, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_720'
}),
(125, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_721'
}),
(125, 174, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_722'
}),
(201, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_723'
}),
(201, 25, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_724'
}),
(201, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_725'
}),
(201, 27, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_726'
}),
(264, 84, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_727'
}),
(264, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_728'
}),
(264, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_729'
}),
(202, 27, {
	'weight': 100,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_730'
}),
(89, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_731'
}),
(89, 127, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_732'
}),
(89, 25, {
	'weight': 850,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_733'
}),
(89, 126, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_734'
}),
(89, 11, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_735'
}),
(89, 203, {
	'weight': 600,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_736'
}),
(89, 128, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_737'
}),
(89, 88, {
	'weight': 650,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_738'
}),
(166, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_739'
}),
(166, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_740'
}),
(166, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_741'
}),
(166, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_742'
}),
(166, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_743'
}),
(167, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_744'
}),
(167, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_745'
}),
(167, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_746'
}),
(167, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_747'
}),
(167, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_748'
}),
(265, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_749'
}),
(265, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_750'
}),
(265, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_751'
}),
(265, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_752'
}),
(49, 48, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_753'
}),
(49, 266, {
	'weight': 200,
	'bw': 2400000,
	'delay': 4,
	'label': 'Link_754'
}),
(140, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_755'
}),
(140, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_756'
}),
(140, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_757'
}),
(65, 267, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_758'
}),
(65, 63, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_759'
}),
(65, 266, {
	'weight': 300,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_760'
}),
(268, 14, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_761'
}),
(268, 269, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_762'
}),
(34, 116, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_763'
}),
(34, 250, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_764'
}),
(34, 270, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_765'
}),
(34, 177, {
	'weight': 750,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_766'
}),
(34, 253, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_767'
}),
(34, 255, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_768'
}),
(34, 28, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_769'
}),
(34, 269, {
	'weight': 350,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_770'
}),
(34, 47, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_771'
}),
(34, 118, {
	'weight': 250,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_772'
}),
(34, 120, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_773'
}),
(34, 254, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_774'
}),
(34, 121, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_775'
}),
(34, 251, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_776'
}),
(34, 252, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_777'
}),
(34, 117, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_778'
}),
(34, 119, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_779'
}),
(34, 70, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_780'
}),
(34, 258, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_781'
}),
(34, 147, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_782'
}),
(34, 16, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_783'
}),
(34, 182, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_784'
}),
(34, 257, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_785'
}),
(34, 256, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_786'
}),
(34, 228, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_787'
}),
(228, 250, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_788'
}),
(228, 147, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_789'
}),
(228, 227, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_790'
}),
(228, 271, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_791'
}),
(228, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_792'
}),
(228, 257, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_793'
}),
(228, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_794'
}),
(75, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_795'
}),
(75, 225, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_796'
}),
(75, 272, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_797'
}),
(75, 76, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_798'
}),
(75, 152, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_799'
}),
(75, 108, {
	'weight': 1250,
	'bw': 10000000,
	'delay': 10,
	'label': 'Link_800'
}),
(75, 232, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_801'
}),
(75, 196, {
	'weight': 750,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_802'
}),
(75, 235, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_803'
}),
(75, 234, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_804'
}),
(75, 233, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_805'
}),
(75, 73, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_806'
}),
(75, 236, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_807'
}),
(75, 237, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_808'
}),
(75, 87, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_809'
}),
(75, 238, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_810'
}),
(224, 222, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_811'
}),
(224, 39, {
	'weight': 850,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_812'
}),
(224, 76, {
	'weight': 650,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_813'
}),
(59, 3, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_814'
}),
(59, 61, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_815'
}),
(59, 58, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_816'
}),
(225, 75, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_817'
}),
(225, 130, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_818'
}),
(225, 222, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_819'
}),
(225, 197, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_820'
}),
(225, 39, {
	'weight': 750,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_821'
}),
(225, 76, {
	'weight': 550,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_822'
}),
(273, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_823'
}),
(273, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_824'
}),
(100, 1, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_825'
}),
(100, 18, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_826'
}),
(100, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_827'
}),
(100, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_828'
}),
(100, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_829'
}),
(164, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_830'
}),
(164, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_831'
}),
(164, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_832'
}),
(164, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_833'
}),
(164, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_834'
}),
(19, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_835'
}),
(19, 90, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_836'
}),
(19, 24, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_837'
}),
(19, 92, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_838'
}),
(19, 93, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_839'
}),
(19, 94, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_840'
}),
(19, 17, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_841'
}),
(19, 95, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_842'
}),
(19, 8, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_843'
}),
(19, 100, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_844'
}),
(19, 101, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_845'
}),
(19, 103, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_846'
}),
(19, 102, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_847'
}),
(19, 274, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_848'
}),
(19, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_849'
}),
(19, 104, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_850'
}),
(19, 105, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_851'
}),
(19, 20, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_852'
}),
(19, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_853'
}),
(19, 106, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_854'
}),
(204, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_855'
}),
(204, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_856'
}),
(204, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_857'
}),
(204, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_858'
}),
(204, 27, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_859'
}),
(205, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_860'
}),
(205, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_861'
}),
(205, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_862'
}),
(205, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_863'
}),
(205, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_864'
}),
(275, 276, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_865'
}),
(275, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_866'
}),
(275, 178, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_867'
}),
(277, 14, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_868'
}),
(277, 152, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_869'
}),
(277, 177, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_870'
}),
(277, 178, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_871'
}),
(142, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_872'
}),
(142, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_873'
}),
(142, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_874'
}),
(276, 178, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_875'
}),
(276, 223, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_876'
}),
(276, 275, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_877'
}),
(134, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_878'
}),
(134, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_879'
}),
(135, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_880'
}),
(135, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_881'
}),
(57, 138, {
	'weight': 400,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_882'
}),
(57, 24, {
	'weight': 550,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_883'
}),
(57, 144, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_884'
}),
(57, 56, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_885'
}),
(57, 137, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_886'
}),
(57, 149, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_887'
}),
(57, 150, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_888'
}),
(57, 151, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_889'
}),
(57, 14, {
	'weight': 650,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_890'
}),
(57, 139, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_891'
}),
(57, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_892'
}),
(57, 68, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_893'
}),
(57, 140, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_894'
}),
(57, 127, {
	'weight': 800,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_895'
}),
(57, 141, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_896'
}),
(57, 4, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_897'
}),
(57, 142, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_898'
}),
(57, 143, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_899'
}),
(57, 146, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_900'
}),
(57, 145, {
	'weight': 350,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_901'
}),
(147, 250, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_902'
}),
(147, 278, {
	'weight': 900,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_903'
}),
(147, 279, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_904'
}),
(147, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_905'
}),
(147, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_906'
}),
(147, 137, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_907'
}),
(147, 228, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_908'
}),
(147, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_909'
}),
(280, 50, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_910'
}),
(280, 281, {
	'weight': 200,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_911'
}),
(256, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_912'
}),
(256, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_913'
}),
(256, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_914'
}),
(250, 147, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_915'
}),
(250, 271, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_916'
}),
(250, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_917'
}),
(250, 115, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_918'
}),
(250, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_919'
}),
(250, 228, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_920'
}),
(278, 14, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_921'
}),
(278, 152, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_922'
}),
(278, 177, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_923'
}),
(278, 178, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_924'
}),
(278, 147, {
	'weight': 900,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_925'
}),
(197, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_926'
}),
(197, 130, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_927'
}),
(197, 225, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_928'
}),
(197, 26, {
	'weight': 1100,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_929'
}),
(197, 230, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_930'
}),
(197, 27, {
	'weight': 900,
	'bw': 10000000,
	'delay': 12,
	'label': 'Link_931'
}),
(197, 32, {
	'weight': 850,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_932'
}),
(197, 76, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_933'
}),
(253, 282, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_934'
}),
(253, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_935'
}),
(253, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_936'
}),
(253, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_937'
}),
(245, 108, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_938'
}),
(245, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_939'
}),
(283, 84, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_940'
}),
(283, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_941'
}),
(283, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_942'
}),
(283, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_943'
}),
(25, 284, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_944'
}),
(25, 2, {
	'weight': 750,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_945'
}),
(25, 60, {
	'weight': 1350,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_946'
}),
(25, 192, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_947'
}),
(25, 191, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_948'
}),
(25, 22, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_949'
}),
(25, 27, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_950'
}),
(25, 36, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_951'
}),
(25, 128, {
	'weight': 750,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_952'
}),
(25, 221, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_953'
}),
(25, 201, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_954'
}),
(25, 99, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_955'
}),
(25, 126, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_956'
}),
(25, 89, {
	'weight': 850,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_957'
}),
(25, 11, {
	'weight': 750,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_958'
}),
(25, 208, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_959'
}),
(25, 211, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_960'
}),
(25, 212, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_961'
}),
(25, 88, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_962'
}),
(25, 21, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_963'
}),
(25, 1, {
	'weight': 700,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_964'
}),
(25, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_965'
}),
(25, 110, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_966'
}),
(25, 198, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_967'
}),
(25, 26, {
	'weight': 400,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_968'
}),
(25, 113, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_969'
}),
(25, 239, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_970'
}),
(25, 114, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_971'
}),
(25, 199, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_972'
}),
(25, 273, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_973'
}),
(25, 203, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_974'
}),
(25, 205, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_975'
}),
(25, 204, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_976'
}),
(25, 108, {
	'weight': 550,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_977'
}),
(25, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_978'
}),
(25, 127, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_979'
}),
(25, 101, {
	'weight': 750,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_980'
}),
(25, 206, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_981'
}),
(25, 207, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_982'
}),
(25, 5, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_983'
}),
(25, 209, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_984'
}),
(25, 210, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_985'
}),
(25, 170, {
	'weight': 750,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_986'
}),
(25, 214, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_987'
}),
(25, 213, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_988'
}),
(193, 241, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_989'
}),
(193, 42, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_990'
}),
(285, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_991'
}),
(285, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_992'
}),
(285, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_993'
}),
(285, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_994'
}),
(153, 200, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_995'
}),
(153, 138, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_996'
}),
(153, 286, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_997'
}),
(153, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_998'
}),
(153, 145, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_999'
}),
(153, 287, {
	'weight': 450,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1000'
}),
(238, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1001'
}),
(238, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1002'
}),
(238, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1003'
}),
(155, 3, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1004'
}),
(155, 181, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1005'
}),
(155, 288, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1006'
}),
(155, 157, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1007'
}),
(155, 128, {
	'weight': 350,
	'bw': 10000000,
	'delay': 15,
	'label': 'Link_1008'
}),
(29, 116, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1009'
}),
(29, 117, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1010'
}),
(29, 119, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1011'
}),
(29, 120, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1012'
}),
(29, 28, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1013'
}),
(29, 122, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1014'
}),
(29, 121, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1015'
}),
(219, 108, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1016'
}),
(219, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1017'
}),
(219, 215, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1018'
}),
(219, 24, {
	'weight': 950,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_1019'
}),
(219, 78, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1020'
}),
(219, 79, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1021'
}),
(289, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1022'
}),
(289, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1023'
}),
(289, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1024'
}),
(289, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1025'
}),
(108, 75, {
	'weight': 1250,
	'bw': 10000000,
	'delay': 10,
	'label': 'Link_1026'
}),
(108, 81, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1027'
}),
(108, 215, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1028'
}),
(108, 107, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1029'
}),
(108, 216, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1030'
}),
(108, 245, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1031'
}),
(108, 217, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1032'
}),
(108, 78, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1033'
}),
(108, 290, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1034'
}),
(108, 79, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1035'
}),
(108, 218, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1036'
}),
(108, 291, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1037'
}),
(108, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1038'
}),
(108, 219, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1039'
}),
(108, 25, {
	'weight': 550,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1040'
}),
(292, 84, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1041'
}),
(292, 196, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1042'
}),
(292, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1043'
}),
(292, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1044'
}),
(23, 192, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1045'
}),
(23, 191, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1046'
}),
(23, 22, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1047'
}),
(23, 27, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1048'
}),
(23, 78, {
	'weight': 550,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_1049'
}),
(23, 36, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1050'
}),
(23, 79, {
	'weight': 500,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1051'
}),
(23, 128, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1052'
}),
(23, 97, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1053'
}),
(23, 99, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1054'
}),
(23, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1055'
}),
(23, 208, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1056'
}),
(23, 212, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1057'
}),
(23, 211, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1058'
}),
(23, 88, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1059'
}),
(23, 1, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_1060'
}),
(23, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1061'
}),
(23, 110, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1062'
}),
(23, 198, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1063'
}),
(23, 26, {
	'weight': 400,
	'bw': 10000000,
	'delay': 13,
	'label': 'Link_1064'
}),
(23, 113, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1065'
}),
(23, 239, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1066'
}),
(23, 199, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1067'
}),
(23, 273, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1068'
}),
(23, 203, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1069'
}),
(23, 205, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1070'
}),
(23, 204, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1071'
}),
(23, 69, {
	'weight': 550,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_1072'
}),
(23, 206, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1073'
}),
(23, 5, {
	'weight': 1000,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_1074'
}),
(23, 207, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1075'
}),
(23, 209, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1076'
}),
(23, 210, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1077'
}),
(23, 214, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1078'
}),
(23, 213, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1079'
}),
(117, 29, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1080'
}),
(117, 31, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1081'
}),
(117, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1082'
}),
(117, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1083'
}),
(117, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1084'
}),
(117, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1085'
}),
(55, 51, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1086'
}),
(55, 53, {
	'weight': 750,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1087'
}),
(5, 1, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1088'
}),
(5, 0, {
	'weight': 850,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1089'
}),
(5, 92, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1090'
}),
(5, 18, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1091'
}),
(5, 93, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1092'
}),
(5, 12, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1093'
}),
(5, 17, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1094'
}),
(5, 94, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1095'
}),
(5, 95, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1096'
}),
(5, 97, {
	'weight': 800,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_1097'
}),
(5, 96, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1098'
}),
(5, 98, {
	'weight': 1000,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1099'
}),
(5, 51, {
	'weight': 700,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_1100'
}),
(5, 25, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_1101'
}),
(5, 19, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1102'
}),
(5, 23, {
	'weight': 1000,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_1103'
}),
(5, 101, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1104'
}),
(5, 103, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1105'
}),
(5, 102, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1106'
}),
(5, 104, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1107'
}),
(5, 105, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1108'
}),
(5, 106, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1109'
}),
(5, 21, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1110'
}),
(15, 267, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1111'
}),
(15, 293, {
	'weight': 500,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1112'
}),
(15, 13, {
	'weight': 300,
	'bw': 10000000,
	'delay': 33,
	'label': 'Link_1113'
}),
(15, 63, {
	'weight': 450,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1114'
}),
(210, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1115'
}),
(210, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1116'
}),
(210, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1117'
}),
(210, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1118'
}),
(210, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1119'
}),
(157, 109, {
	'weight': 650,
	'bw': 10000000,
	'delay': 14,
	'label': 'Link_1120'
}),
(157, 3, {
	'weight': 300,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1121'
}),
(157, 155, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1122'
}),
(157, 181, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1123'
}),
(157, 288, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1124'
}),
(138, 286, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1125'
}),
(138, 200, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1126'
}),
(138, 24, {
	'weight': 750,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1127'
}),
(138, 153, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1128'
}),
(138, 57, {
	'weight': 400,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1129'
}),
(138, 175, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1130'
}),
(138, 287, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1131'
}),
(138, 137, {
	'weight': 300,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1132'
}),
(294, 152, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1133'
}),
(294, 295, {
	'weight': 900,
	'bw': 10000000,
	'delay': 29,
	'label': 'Link_1134'
}),
(294, 296, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1135'
}),
(297, 14, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1136'
}),
(297, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1137'
}),
(297, 177, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1138'
}),
(297, 178, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1139'
}),
(255, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1140'
}),
(255, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1141'
}),
(255, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1142'
}),
(84, 298, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1143'
}),
(84, 195, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1144'
}),
(84, 76, {
	'weight': 850,
	'bw': 2400000,
	'delay': 21,
	'label': 'Link_1145'
}),
(84, 243, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1146'
}),
(84, 242, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1147'
}),
(84, 8, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1148'
}),
(84, 264, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1149'
}),
(84, 283, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1150'
}),
(84, 126, {
	'weight': 1200,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_1151'
}),
(84, 289, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1152'
}),
(84, 299, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1153'
}),
(84, 300, {
	'weight': 600,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1154'
}),
(84, 301, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1155'
}),
(84, 265, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1156'
}),
(84, 292, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1157'
}),
(84, 285, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1158'
}),
(84, 302, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1159'
}),
(84, 82, {
	'weight': 250,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_1160'
}),
(84, 54, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1161'
}),
(121, 29, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1162'
}),
(121, 30, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1163'
}),
(121, 31, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1164'
}),
(121, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1165'
}),
(121, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1166'
}),
(121, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1167'
}),
(121, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1168'
}),
(266, 49, {
	'weight': 200,
	'bw': 2400000,
	'delay': 4,
	'label': 'Link_1169'
}),
(266, 281, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1170'
}),
(266, 65, {
	'weight': 300,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1171'
}),
(301, 84, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1172'
}),
(301, 196, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1173'
}),
(301, 54, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1174'
}),
(301, 85, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1175'
}),
(222, 224, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1176'
}),
(222, 225, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1177'
}),
(222, 168, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1178'
}),
(222, 303, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1179'
}),
(222, 263, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1180'
}),
(222, 304, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1181'
}),
(222, 305, {
	'weight': 750,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1182'
}),
(222, 126, {
	'weight': 600,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1183'
}),
(183, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1184'
}),
(183, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1185'
}),
(282, 253, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1186'
}),
(119, 29, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1187'
}),
(119, 30, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1188'
}),
(119, 31, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1189'
}),
(119, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1190'
}),
(119, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1191'
}),
(119, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1192'
}),
(119, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1193'
}),
(279, 147, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1194'
}),
(168, 222, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1195'
}),
(168, 127, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1196'
}),
(168, 306, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1197'
}),
(168, 263, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1198'
}),
(168, 76, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1199'
}),
(168, 304, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1200'
}),
(271, 250, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1201'
}),
(271, 228, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1202'
}),
(263, 125, {
	'weight': 500,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1203'
}),
(263, 222, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1204'
}),
(263, 168, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1205'
}),
(188, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1206'
}),
(188, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1207'
}),
(145, 286, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1208'
}),
(145, 200, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1209'
}),
(145, 24, {
	'weight': 900,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1210'
}),
(145, 153, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1211'
}),
(145, 57, {
	'weight': 350,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1212'
}),
(145, 175, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1213'
}),
(145, 137, {
	'weight': 350,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1214'
}),
(145, 287, {
	'weight': 700,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1215'
}),
(293, 307, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1216'
}),
(293, 15, {
	'weight': 500,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1217'
}),
(169, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1218'
}),
(169, 125, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1219'
}),
(169, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1220'
}),
(169, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1221'
}),
(169, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1222'
}),
(169, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1223'
}),
(44, 152, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1224'
}),
(44, 45, {
	'weight': 750,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_1225'
}),
(44, 40, {
	'weight': 950,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_1226'
}),
(46, 45, {
	'weight': 900,
	'bw': 2400000,
	'delay': 29,
	'label': 'Link_1227'
}),
(46, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1228'
}),
(46, 296, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1229'
}),
(270, 308, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1230'
}),
(270, 34, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1231'
}),
(308, 270, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1232'
}),
(308, 32, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1233'
}),
(26, 197, {
	'weight': 1100,
	'bw': 2400000,
	'delay': 2,
	'label': 'Link_1234'
}),
(26, 24, {
	'weight': 400,
	'bw': 10000000,
	'delay': 13,
	'label': 'Link_1235'
}),
(26, 192, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1236'
}),
(26, 191, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1237'
}),
(26, 110, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1238'
}),
(26, 18, {
	'weight': 600,
	'bw': 2400000,
	'delay': 21,
	'label': 'Link_1239'
}),
(26, 198, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1240'
}),
(26, 113, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1241'
}),
(26, 22, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1242'
}),
(26, 78, {
	'weight': 650,
	'bw': 2400000,
	'delay': 10,
	'label': 'Link_1243'
}),
(26, 36, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1244'
}),
(26, 199, {
	'weight': 500,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1245'
}),
(26, 200, {
	'weight': 850,
	'bw': 2400000,
	'delay': 9,
	'label': 'Link_1246'
}),
(26, 99, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1247'
}),
(26, 201, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1248'
}),
(26, 25, {
	'weight': 400,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1249'
}),
(26, 203, {
	'weight': 650,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1250'
}),
(26, 204, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1251'
}),
(26, 205, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1252'
}),
(26, 124, {
	'weight': 750,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_1253'
}),
(26, 23, {
	'weight': 400,
	'bw': 10000000,
	'delay': 13,
	'label': 'Link_1254'
}),
(26, 206, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1255'
}),
(26, 207, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1256'
}),
(26, 208, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1257'
}),
(26, 209, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1258'
}),
(26, 210, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1259'
}),
(26, 211, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1260'
}),
(26, 212, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1261'
}),
(26, 88, {
	'weight': 400,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1262'
}),
(26, 213, {
	'weight': 250,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1263'
}),
(26, 214, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1264'
}),
(179, 14, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1265'
}),
(179, 152, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1266'
}),
(179, 259, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1267'
}),
(179, 177, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1268'
}),
(179, 178, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1269'
}),
(179, 176, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1270'
}),
(306, 168, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1271'
}),
(306, 303, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1272'
}),
(32, 116, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1273'
}),
(32, 308, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1274'
}),
(32, 253, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1275'
}),
(32, 197, {
	'weight': 850,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1276'
}),
(32, 255, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1277'
}),
(32, 28, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1278'
}),
(32, 118, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1279'
}),
(32, 254, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1280'
}),
(32, 120, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1281'
}),
(32, 122, {
	'weight': 350,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1282'
}),
(32, 121, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1283'
}),
(32, 69, {
	'weight': 400,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_1284'
}),
(32, 117, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1285'
}),
(32, 252, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1286'
}),
(32, 251, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1287'
}),
(32, 119, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1288'
}),
(32, 70, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1289'
}),
(32, 4, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1290'
}),
(32, 258, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1291'
}),
(32, 6, {
	'weight': 600,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1292'
}),
(32, 147, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1293'
}),
(32, 227, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1294'
}),
(32, 256, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1295'
}),
(32, 257, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1296'
}),
(32, 228, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1297'
}),
(76, 224, {
	'weight': 650,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1298'
}),
(76, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1299'
}),
(76, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1300'
}),
(76, 130, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1301'
}),
(76, 225, {
	'weight': 550,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1302'
}),
(76, 197, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1303'
}),
(76, 223, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1304'
}),
(76, 84, {
	'weight': 850,
	'bw': 2400000,
	'delay': 21,
	'label': 'Link_1305'
}),
(76, 232, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1306'
}),
(76, 168, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1307'
}),
(76, 233, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1308'
}),
(76, 234, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1309'
}),
(76, 85, {
	'weight': 750,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1310'
}),
(76, 73, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1311'
}),
(76, 236, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1312'
}),
(76, 237, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1313'
}),
(76, 87, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1314'
}),
(76, 257, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1315'
}),
(76, 238, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1316'
}),
(120, 29, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1317'
}),
(120, 30, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1318'
}),
(120, 31, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1319'
}),
(120, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1320'
}),
(120, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1321'
}),
(120, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1322'
}),
(120, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1323'
}),
(122, 29, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1324'
}),
(122, 30, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1325'
}),
(122, 31, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1326'
}),
(122, 32, {
	'weight': 350,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1327'
}),
(122, 33, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1328'
}),
(299, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1329'
}),
(299, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1330'
}),
(299, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1331'
}),
(299, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1332'
}),
(68, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1333'
}),
(68, 67, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1334'
}),
(68, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1335'
}),
(68, 88, {
	'weight': 750,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_1336'
}),
(101, 5, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1337'
}),
(101, 1, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1338'
}),
(101, 18, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1339'
}),
(101, 25, {
	'weight': 750,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_1340'
}),
(101, 19, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1341'
}),
(101, 20, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1342'
}),
(101, 21, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1343'
}),
(249, 247, {
	'weight': 450,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_1344'
}),
(249, 196, {
	'weight': 700,
	'bw': 10000000,
	'delay': 44,
	'label': 'Link_1345'
}),
(249, 62, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1346'
}),
(206, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1347'
}),
(206, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1348'
}),
(206, 25, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1349'
}),
(206, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1350'
}),
(206, 27, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1351'
}),
(218, 108, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1352'
}),
(218, 78, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1353'
}),
(218, 79, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1354'
}),
(244, 8, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1355'
}),
(106, 1, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1356'
}),
(106, 5, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1357'
}),
(106, 18, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1358'
}),
(106, 19, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1359'
}),
(106, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1360'
}),
(106, 21, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1361'
}),
(248, 247, {
	'weight': 1250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1362'
}),
(248, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 57,
	'label': 'Link_1363'
}),
(177, 14, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1364'
}),
(177, 74, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1365'
}),
(177, 278, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1366'
}),
(177, 297, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1367'
}),
(177, 178, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1368'
}),
(177, 179, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1369'
}),
(177, 296, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1370'
}),
(177, 176, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1371'
}),
(177, 277, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1372'
}),
(177, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1373'
}),
(177, 259, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1374'
}),
(177, 34, {
	'weight': 750,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_1375'
}),
(50, 41, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1376'
}),
(50, 48, {
	'weight': 200,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1377'
}),
(50, 280, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1378'
}),
(66, 63, {
	'weight': 100,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1379'
}),
(148, 137, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1380'
}),
(300, 196, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1381'
}),
(300, 84, {
	'weight': 600,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1382'
}),
(300, 85, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1383'
}),
(300, 54, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1384'
}),
(300, 103, {
	'weight': 650,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1385'
}),
(62, 309, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1386'
}),
(62, 247, {
	'weight': 200,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_1387'
}),
(62, 3, {
	'weight': 800,
	'bw': 10000000,
	'delay': 40,
	'label': 'Link_1388'
}),
(62, 310, {
	'weight': 200,
	'bw': 10000000,
	'delay': 28,
	'label': 'Link_1389'
}),
(62, 58, {
	'weight': 600,
	'bw': 10000000,
	'delay': 40,
	'label': 'Link_1390'
}),
(62, 249, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1391'
}),
(190, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1392'
}),
(190, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1393'
}),
(309, 310, {
	'weight': 500,
	'bw': 2400000,
	'delay': 28,
	'label': 'Link_1394'
}),
(309, 196, {
	'weight': 750,
	'bw': 10000000,
	'delay': 44,
	'label': 'Link_1395'
}),
(309, 62, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1396'
}),
(196, 75, {
	'weight': 750,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1397'
}),
(196, 231, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1398'
}),
(196, 298, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1399'
}),
(196, 2, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1400'
}),
(196, 53, {
	'weight': 300,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1401'
}),
(196, 195, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1402'
}),
(196, 243, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1403'
}),
(196, 283, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1404'
}),
(196, 289, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1405'
}),
(196, 300, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1406'
}),
(196, 299, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1407'
}),
(196, 301, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1408'
}),
(196, 309, {
	'weight': 750,
	'bw': 10000000,
	'delay': 44,
	'label': 'Link_1409'
}),
(196, 265, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1410'
}),
(196, 292, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1411'
}),
(196, 285, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1412'
}),
(196, 302, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1413'
}),
(196, 249, {
	'weight': 700,
	'bw': 10000000,
	'delay': 44,
	'label': 'Link_1414'
}),
(196, 261, {
	'weight': 200,
	'bw': 10000000,
	'delay': 62,
	'label': 'Link_1415'
}),
(196, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1416'
}),
(85, 298, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1417'
}),
(85, 53, {
	'weight': 500,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1418'
}),
(85, 195, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1419'
}),
(85, 76, {
	'weight': 750,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1420'
}),
(85, 243, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1421'
}),
(85, 242, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1422'
}),
(85, 8, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1423'
}),
(85, 264, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1424'
}),
(85, 283, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1425'
}),
(85, 126, {
	'weight': 1100,
	'bw': 10000000,
	'delay': 16,
	'label': 'Link_1426'
}),
(85, 289, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1427'
}),
(85, 299, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1428'
}),
(85, 300, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1429'
}),
(85, 301, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1430'
}),
(85, 265, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1431'
}),
(85, 285, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1432'
}),
(85, 292, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1433'
}),
(85, 302, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1434'
}),
(85, 82, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1435'
}),
(85, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1436'
}),
(103, 5, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1437'
}),
(103, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1438'
}),
(103, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1439'
}),
(103, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1440'
}),
(103, 300, {
	'weight': 650,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1441'
}),
(103, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1442'
}),
(103, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1443'
}),
(212, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1444'
}),
(212, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1445'
}),
(212, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1446'
}),
(212, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1447'
}),
(212, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1448'
}),
(178, 14, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1449'
}),
(178, 74, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1450'
}),
(178, 177, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1451'
}),
(178, 278, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1452'
}),
(178, 297, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1453'
}),
(178, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1454'
}),
(178, 179, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1455'
}),
(178, 4, {
	'weight': 750,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1456'
}),
(178, 275, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1457'
}),
(178, 277, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1458'
}),
(178, 176, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1459'
}),
(178, 128, {
	'weight': 1150,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_1460'
}),
(178, 276, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1461'
}),
(178, 305, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1462'
}),
(178, 259, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1463'
}),
(152, 46, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1464'
}),
(152, 75, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1465'
}),
(152, 311, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1466'
}),
(152, 294, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1467'
}),
(152, 312, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1468'
}),
(152, 297, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1469'
}),
(152, 278, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1470'
}),
(152, 177, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1471'
}),
(152, 179, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1472'
}),
(152, 296, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1473'
}),
(152, 128, {
	'weight': 850,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_1474'
}),
(152, 305, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1475'
}),
(152, 14, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1476'
}),
(152, 69, {
	'weight': 650,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1477'
}),
(152, 4, {
	'weight': 550,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1478'
}),
(152, 277, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1479'
}),
(152, 176, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1480'
}),
(152, 259, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1481'
}),
(152, 16, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1482'
}),
(152, 44, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1483'
}),
(254, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1484'
}),
(254, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1485'
}),
(254, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1486'
}),
(313, 2, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1487'
}),
(302, 84, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1488'
}),
(302, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1489'
}),
(302, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1490'
}),
(302, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1491'
}),
(187, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1492'
}),
(187, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1493'
}),
(102, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1494'
}),
(102, 5, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1495'
}),
(102, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1496'
}),
(102, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1497'
}),
(102, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1498'
}),
(102, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1499'
}),
(207, 23, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1500'
}),
(207, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1501'
}),
(207, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1502'
}),
(207, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1503'
}),
(207, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1504'
}),
(16, 152, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1505'
}),
(16, 45, {
	'weight': 450,
	'bw': 10000000,
	'delay': 30,
	'label': 'Link_1506'
}),
(16, 13, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1507'
}),
(16, 34, {
	'weight': 400,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1508'
}),
(16, 40, {
	'weight': 250,
	'bw': 10000000,
	'delay': 30,
	'label': 'Link_1509'
}),
(31, 116, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1510'
}),
(31, 117, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1511'
}),
(31, 118, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1512'
}),
(31, 119, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1513'
}),
(31, 120, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1514'
}),
(31, 28, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1515'
}),
(31, 121, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1516'
}),
(31, 122, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1517'
}),
(170, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1518'
}),
(170, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1519'
}),
(170, 25, {
	'weight': 750,
	'bw': 2400000,
	'delay': 8,
	'label': 'Link_1520'
}),
(170, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1521'
}),
(170, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1522'
}),
(170, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1523'
}),
(287, 200, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1524'
}),
(287, 138, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1525'
}),
(287, 146, {
	'weight': 450,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1526'
}),
(287, 145, {
	'weight': 700,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1527'
}),
(287, 153, {
	'weight': 450,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1528'
}),
(281, 280, {
	'weight': 200,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1529'
}),
(281, 266, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1530'
}),
(105, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1531'
}),
(105, 5, {
	'weight': 900,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1532'
}),
(105, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1533'
}),
(105, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1534'
}),
(105, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1535'
}),
(105, 21, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1536'
}),
(307, 267, {
	'weight': 200,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1537'
}),
(307, 293, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1538'
}),
(267, 307, {
	'weight': 200,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1539'
}),
(267, 41, {
	'weight': 250,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_1540'
}),
(267, 15, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1541'
}),
(267, 65, {
	'weight': 650,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1542'
}),
(41, 267, {
	'weight': 250,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_1543'
}),
(41, 295, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1544'
}),
(41, 50, {
	'weight': 200,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1545'
}),
(41, 42, {
	'weight': 500,
	'bw': 2400000,
	'delay': 3,
	'label': 'Link_1546'
}),
(41, 40, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1547'
}),
(41, 314, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1548'
}),
(284, 24, {
	'weight': 400,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1549'
}),
(284, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1550'
}),
(295, 41, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1551'
}),
(295, 294, {
	'weight': 900,
	'bw': 10000000,
	'delay': 29,
	'label': 'Link_1552'
}),
(223, 276, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1553'
}),
(223, 305, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1554'
}),
(223, 269, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1555'
}),
(223, 14, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1556'
}),
(223, 178, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1557'
}),
(223, 11, {
	'weight': 750,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_1558'
}),
(223, 296, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1559'
}),
(223, 76, {
	'weight': 600,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1560'
}),
(223, 275, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1561'
}),
(53, 1, {
	'weight': 750,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_1562'
}),
(53, 52, {
	'weight': 800,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1563'
}),
(53, 51, {
	'weight': 950,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1564'
}),
(53, 196, {
	'weight': 300,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1565'
}),
(53, 54, {
	'weight': 300,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1566'
}),
(53, 85, {
	'weight': 500,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1567'
}),
(53, 21, {
	'weight': 750,
	'bw': 10000000,
	'delay': 22,
	'label': 'Link_1568'
}),
(53, 55, {
	'weight': 750,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1569'
}),
(269, 305, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1570'
}),
(269, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1571'
}),
(269, 296, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1572'
}),
(269, 268, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1573'
}),
(269, 34, {
	'weight': 350,
	'bw': 10000000,
	'delay': 3,
	'label': 'Link_1574'
}),
(200, 138, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1575'
}),
(200, 286, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1576'
}),
(200, 145, {
	'weight': 450,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1577'
}),
(200, 153, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1578'
}),
(200, 26, {
	'weight': 850,
	'bw': 2400000,
	'delay': 9,
	'label': 'Link_1579'
}),
(200, 27, {
	'weight': 650,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1580'
}),
(200, 287, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1581'
}),
(252, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1582'
}),
(252, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1583'
}),
(252, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1584'
}),
(232, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1585'
}),
(232, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1586'
}),
(232, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1587'
}),
(235, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1588'
}),
(235, 74, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1589'
}),
(258, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1590'
}),
(258, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1591'
}),
(258, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1592'
}),
(236, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1593'
}),
(236, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1594'
}),
(236, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1595'
}),
(208, 23, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1596'
}),
(208, 24, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1597'
}),
(208, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1598'
}),
(208, 25, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1599'
}),
(208, 27, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1600'
}),
(298, 84, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1601'
}),
(298, 196, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1602'
}),
(298, 54, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1603'
}),
(298, 85, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1604'
}),
(90, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1605'
}),
(90, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1606'
}),
(90, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1607'
}),
(90, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1608'
}),
(90, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1609'
}),
(93, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1610'
}),
(93, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1611'
}),
(93, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1612'
}),
(93, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1613'
}),
(93, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1614'
}),
(93, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1615'
}),
(216, 108, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1616'
}),
(216, 109, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1617'
}),
(216, 203, {
	'weight': 700,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_1618'
}),
(216, 78, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1619'
}),
(216, 79, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1620'
}),
(296, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1621'
}),
(296, 269, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1622'
}),
(296, 305, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1623'
}),
(296, 46, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1624'
}),
(296, 311, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1625'
}),
(296, 294, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1626'
}),
(296, 312, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1627'
}),
(296, 177, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1628'
}),
(296, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1629'
}),
(262, 189, {
	'weight': 100,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_1630'
}),
(305, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1631'
}),
(305, 269, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1632'
}),
(305, 222, {
	'weight': 750,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1633'
}),
(305, 178, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1634'
}),
(305, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1635'
}),
(305, 296, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1636'
}),
(61, 59, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1637'
}),
(61, 3, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1638'
}),
(61, 58, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1639'
}),
(288, 155, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1640'
}),
(288, 157, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1641'
}),
(149, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1642'
}),
(149, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1643'
}),
(149, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1644'
}),
(234, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1645'
}),
(234, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1646'
}),
(234, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1647'
}),
(72, 183, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1648'
}),
(72, 185, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1649'
}),
(72, 186, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1650'
}),
(72, 60, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1651'
}),
(72, 3, {
	'weight': 550,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1652'
}),
(72, 71, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1653'
}),
(72, 127, {
	'weight': 800,
	'bw': 2400000,
	'delay': 9,
	'label': 'Link_1654'
}),
(72, 187, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1655'
}),
(72, 188, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1656'
}),
(72, 128, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1657'
}),
(72, 189, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1658'
}),
(72, 11, {
	'weight': 500,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1659'
}),
(72, 190, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1660'
}),
(274, 19, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1661'
}),
(6, 0, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1662'
}),
(6, 8, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1663'
}),
(6, 18, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1664'
}),
(6, 54, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1665'
}),
(6, 10, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1666'
}),
(6, 32, {
	'weight': 600,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1667'
}),
(6, 21, {
	'weight': 550,
	'bw': 2400000,
	'delay': 4,
	'label': 'Link_1668'
}),
(209, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1669'
}),
(209, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1670'
}),
(209, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1671'
}),
(209, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1672'
}),
(209, 27, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1673'
}),
(54, 74, {
	'weight': 650,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1674'
}),
(54, 231, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1675'
}),
(54, 298, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1676'
}),
(54, 248, {
	'weight': 200,
	'bw': 10000000,
	'delay': 57,
	'label': 'Link_1677'
}),
(54, 53, {
	'weight': 300,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1678'
}),
(54, 195, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1679'
}),
(54, 242, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1680'
}),
(54, 243, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1681'
}),
(54, 264, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1682'
}),
(54, 51, {
	'weight': 850,
	'bw': 10000000,
	'delay': 21,
	'label': 'Link_1683'
}),
(54, 283, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1684'
}),
(54, 84, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1685'
}),
(54, 289, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1686'
}),
(54, 300, {
	'weight': 500,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1687'
}),
(54, 299, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1688'
}),
(54, 301, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1689'
}),
(54, 265, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1690'
}),
(54, 285, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1691'
}),
(54, 292, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1692'
}),
(54, 196, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1693'
}),
(54, 302, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1694'
}),
(54, 85, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1695'
}),
(54, 261, {
	'weight': 200,
	'bw': 10000000,
	'delay': 62,
	'label': 'Link_1696'
}),
(54, 83, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1697'
}),
(54, 6, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1698'
}),
(54, 10, {
	'weight': 300,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1699'
}),
(171, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1700'
}),
(171, 126, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1701'
}),
(171, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1702'
}),
(171, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1703'
}),
(171, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1704'
}),
(173, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1705'
}),
(173, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1706'
}),
(173, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1707'
}),
(173, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1708'
}),
(173, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1709'
}),
(214, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1710'
}),
(214, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1711'
}),
(214, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1712'
}),
(214, 26, {
	'weight': 300,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1713'
}),
(214, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1714'
}),
(311, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1715'
}),
(311, 296, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1716'
}),
(2, 0, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1717'
}),
(2, 8, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1718'
}),
(2, 25, {
	'weight': 750,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1719'
}),
(2, 196, {
	'weight': 500,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1720'
}),
(2, 313, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1721'
}),
(2, 10, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1722'
}),
(2, 21, {
	'weight': 250,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1723'
}),
(312, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1724'
}),
(312, 296, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1725'
}),
(185, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1726'
}),
(185, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1727'
}),
(154, 133, {
	'weight': 1300,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_1728'
}),
(154, 3, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1729'
}),
(310, 309, {
	'weight': 500,
	'bw': 2400000,
	'delay': 28,
	'label': 'Link_1730'
}),
(310, 62, {
	'weight': 200,
	'bw': 10000000,
	'delay': 28,
	'label': 'Link_1731'
}),
(217, 108, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1732'
}),
(217, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1733'
}),
(217, 78, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1734'
}),
(217, 79, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1735'
}),
(162, 124, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1736'
}),
(162, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1737'
}),
(162, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1738'
}),
(162, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1739'
}),
(162, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1740'
}),
(144, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1741'
}),
(144, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1742'
}),
(144, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1743'
}),
(133, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1744'
}),
(133, 154, {
	'weight': 1300,
	'bw': 2400000,
	'delay': 16,
	'label': 'Link_1745'
}),
(133, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1746'
}),
(115, 250, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1747'
}),
(115, 113, {
	'weight': 1550,
	'bw': 2400000,
	'delay': 11,
	'label': 'Link_1748'
}),
(115, 4, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1749'
}),
(286, 200, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1750'
}),
(286, 138, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1751'
}),
(286, 145, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1752'
}),
(286, 153, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1753'
}),
(186, 72, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1754'
}),
(186, 60, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1755'
}),
(251, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1756'
}),
(251, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1757'
}),
(251, 34, {
	'weight': 250,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1758'
}),
(156, 3, {
	'weight': 650,
	'bw': 10000000,
	'delay': 64,
	'label': 'Link_1759'
}),
(156, 260, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1760'
}),
(261, 260, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1761'
}),
(261, 196, {
	'weight': 200,
	'bw': 10000000,
	'delay': 62,
	'label': 'Link_1762'
}),
(261, 54, {
	'weight': 200,
	'bw': 10000000,
	'delay': 62,
	'label': 'Link_1763'
}),
(143, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1764'
}),
(143, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1765'
}),
(143, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1766'
}),
(241, 64, {
	'weight': 600,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1767'
}),
(241, 193, {
	'weight': 200,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1768'
}),
(211, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1769'
}),
(211, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1770'
}),
(211, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1771'
}),
(211, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1772'
}),
(211, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1773'
}),
(172, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1774'
}),
(172, 125, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1775'
}),
(172, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1776'
}),
(172, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1777'
}),
(172, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1778'
}),
(172, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1779'
}),
(116, 29, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1780'
}),
(116, 30, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1781'
}),
(116, 31, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1782'
}),
(116, 32, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1783'
}),
(116, 4, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1784'
}),
(116, 34, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1785'
}),
(116, 33, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1786'
}),
(272, 75, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1787'
}),
(81, 108, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1788'
}),
(81, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1789'
}),
(81, 80, {
	'weight': 100,
	'bw': 10000000,
	'delay': 6,
	'label': 'Link_1790'
}),
(81, 78, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1791'
}),
(81, 79, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1792'
}),
(92, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1793'
}),
(92, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1794'
}),
(92, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1795'
}),
(92, 19, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1796'
}),
(92, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1797'
}),
(92, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1798'
}),
(24, 284, {
	'weight': 400,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1799'
}),
(24, 138, {
	'weight': 750,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1800'
}),
(24, 192, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1801'
}),
(24, 191, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1802'
}),
(24, 22, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1803'
}),
(24, 27, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1804'
}),
(24, 36, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1805'
}),
(24, 221, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1806'
}),
(24, 201, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1807'
}),
(24, 99, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1808'
}),
(24, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1809'
}),
(24, 145, {
	'weight': 900,
	'bw': 10000000,
	'delay': 9,
	'label': 'Link_1810'
}),
(24, 208, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1811'
}),
(24, 211, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1812'
}),
(24, 212, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1813'
}),
(24, 88, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1814'
}),
(24, 74, {
	'weight': 900,
	'bw': 10000000,
	'delay': 12,
	'label': 'Link_1815'
}),
(24, 110, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1816'
}),
(24, 198, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1817'
}),
(24, 26, {
	'weight': 400,
	'bw': 10000000,
	'delay': 13,
	'label': 'Link_1818'
}),
(24, 113, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1819'
}),
(24, 114, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1820'
}),
(24, 199, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1821'
}),
(24, 109, {
	'weight': 550,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1822'
}),
(24, 219, {
	'weight': 950,
	'bw': 2400000,
	'delay': 5,
	'label': 'Link_1823'
}),
(24, 19, {
	'weight': 400,
	'bw': 10000000,
	'delay': 11,
	'label': 'Link_1824'
}),
(24, 203, {
	'weight': 350,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1825'
}),
(24, 205, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1826'
}),
(24, 204, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1827'
}),
(24, 23, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1828'
}),
(24, 206, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1829'
}),
(24, 207, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1830'
}),
(24, 209, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1831'
}),
(24, 210, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1832'
}),
(24, 57, {
	'weight': 550,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_1833'
}),
(24, 214, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1834'
}),
(24, 213, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1835'
}),
(215, 108, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1836'
}),
(215, 109, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1837'
}),
(215, 219, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1838'
}),
(215, 78, {
	'weight': 400,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1839'
}),
(215, 79, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1840'
}),
(198, 23, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1841'
}),
(198, 24, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1842'
}),
(198, 25, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1843'
}),
(198, 26, {
	'weight': 200,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1844'
}),
(198, 27, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1845'
}),
(94, 1, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1846'
}),
(94, 5, {
	'weight': 750,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1847'
}),
(94, 18, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1848'
}),
(94, 19, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1849'
}),
(94, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1850'
}),
(94, 21, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1851'
}),
(114, 24, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1852'
}),
(114, 25, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1853'
}),
(114, 113, {
	'weight': 500,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1854'
}),
(304, 222, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1855'
}),
(304, 168, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1856'
}),
(52, 51, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1857'
}),
(52, 53, {
	'weight': 800,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1858'
}),
(136, 38, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1859'
}),
(136, 39, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1860'
}),
(150, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1861'
}),
(150, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1862'
}),
(150, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1863'
}),
(151, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1864'
}),
(151, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1865'
}),
(151, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1866'
}),
(229, 181, {
	'weight': 100,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1867'
}),
(14, 177, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1868'
}),
(14, 278, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1869'
}),
(14, 297, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1870'
}),
(14, 13, {
	'weight': 450,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1871'
}),
(14, 178, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1872'
}),
(14, 223, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1873'
}),
(14, 127, {
	'weight': 850,
	'bw': 10000000,
	'delay': 7,
	'label': 'Link_1874'
}),
(14, 179, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1875'
}),
(14, 277, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1876'
}),
(14, 268, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1877'
}),
(14, 176, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1878'
}),
(14, 152, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1879'
}),
(14, 259, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1880'
}),
(14, 57, {
	'weight': 650,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1881'
}),
(124, 26, {
	'weight': 750,
	'bw': 2400000,
	'delay': 7,
	'label': 'Link_1882'
}),
(124, 158, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1883'
}),
(124, 27, {
	'weight': 550,
	'bw': 10000000,
	'delay': 8,
	'label': 'Link_1884'
}),
(124, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1885'
}),
(124, 162, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1886'
}),
(124, 123, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1887'
}),
(124, 125, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1888'
}),
(124, 129, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1889'
}),
(124, 164, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1890'
}),
(124, 89, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1891'
}),
(124, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1892'
}),
(124, 165, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1893'
}),
(124, 166, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1894'
}),
(124, 167, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1895'
}),
(124, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1896'
}),
(124, 169, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1897'
}),
(124, 172, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1898'
}),
(124, 171, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1899'
}),
(124, 170, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1900'
}),
(124, 173, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1901'
}),
(124, 174, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1902'
}),
(184, 60, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1903'
}),
(233, 74, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1904'
}),
(233, 75, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1905'
}),
(233, 76, {
	'weight': 300,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1906'
}),
(303, 222, {
	'weight': 250,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1907'
}),
(303, 306, {
	'weight': 300,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1908'
}),
(141, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1909'
}),
(141, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1910'
}),
(141, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1911'
}),
(314, 41, {
	'weight': 100,
	'bw': 10000000,
	'delay': 4,
	'label': 'Link_1912'
}),
(290, 108, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1913'
}),
(246, 109, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1914'
}),
(7, 0, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1915'
}),
(7, 10, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1916'
}),
(146, 69, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1917'
}),
(146, 57, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1918'
}),
(146, 137, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1919'
}),
(146, 287, {
	'weight': 450,
	'bw': 10000000,
	'delay': 5,
	'label': 'Link_1920'
}),
(291, 108, {
	'weight': 100,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1921'
}),
(104, 5, {
	'weight': 800,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1922'
}),
(104, 1, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1923'
}),
(104, 18, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1924'
}),
(104, 19, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1925'
}),
(104, 20, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1926'
}),
(104, 21, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1927'
}),
(10, 0, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1928'
}),
(10, 2, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1929'
}),
(10, 6, {
	'weight': 400,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1930'
}),
(10, 7, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1931'
}),
(10, 54, {
	'weight': 300,
	'bw': 10000000,
	'delay': 2,
	'label': 'Link_1932'
}),
(213, 23, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1933'
}),
(213, 24, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1934'
}),
(213, 25, {
	'weight': 250,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1935'
}),
(213, 26, {
	'weight': 250,
	'bw': 2400000,
	'delay': 13,
	'label': 'Link_1936'
}),
(213, 27, {
	'weight': 350,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1937'
}),
(174, 124, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1938'
}),
(174, 125, {
	'weight': 200,
	'bw': 2400000,
	'delay': 1,
	'label': 'Link_1939'
}),
(174, 126, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1940'
}),
(174, 127, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1941'
}),
(174, 11, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1942'
}),
(174, 128, {
	'weight': 200,
	'bw': 10000000,
	'delay': 1,
	'label': 'Link_1943'
}),
])

n_nodes = network.number_of_nodes()
list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table

#net_dist = dict(nx.all_pairs_dijkstra_path_length(network))

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