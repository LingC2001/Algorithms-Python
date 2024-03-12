import pytest
import sys
sys.path.append("./")
from bucket_sort import bucket_sort
import random

def test_empty():
    arr = []
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_already_sorted():
    arr = [1, 2, 5, 6, 9, 11]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_reverse_sorted():
    arr = [19, 11, 8, 5, 2, 0]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_normal_sort():
    arr = [1, 7, 2, 8, 7, 1, 4, 10, 22]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_negative_nums():
    arr = [1, 7, 2, -8, 7, -1, 4, -10, 22]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_negative_nums_only():
    arr = [-1, -7, -2, -8, -7, -1, -4, -10, -22]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_decimals():
    arr = [1.4, 7, 2.2, -8.1, 7, -1, 4.0, -10.123, 22]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_large_inputs():
    arr = [3,-9223372036854775807, 2, -1, 9223372036854775807]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_larger_inputs():
    arr = [3,-92233720368547758077454574, 2, -1, 9223372036854775804574574577]
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted

def test_large_arr():
    arr = [-99780, -99708, -99260, -99080, -98986, -98870, -98824, -98771, -98585, -98430, -98042, -97861, -97832, -97783, -97702, -97694, -97568, -97531, -97398, -97355, -97315, -97294, -97229, -97014, -96506, -96491, -96412, -96076, -96045, -95908, -95786, -95781, -95600, -95575, -95489, -95485, -95420, -95273, -95262, -95117, -94916, -94769, -94755, -94730, -94522, -94156, -93972, -93871, -93363, -93255, -92810, -92344, -92133, -91750, -91679, -91540, -91529, -91060, -91056, -90977, -90555, -90308, -89043, -88851, -88714, -88485, -88462, -88415, -88401, -88354, -88339, -87838, -87312, -87147, -87032, -86867, -86402, -86338, -86305, -86291, -86218, -86025, -85941, -85272, -85063, -84816, -84648, -84582, -84448, -84415, -84339, -83971, -83867, -83741, -83561, -83447, -83202, -83053, -82974, -82623, -82621, -82588, -82180, -81596, -81529, -81429, -81348, -81245, -80975, -80953, -80587, -80225, -80078, -79899, -79836, -79734, -79708, -79553, -79371, -79291, -78945, -78619, -78488, -78452, -78185, -77936, -77916, -77814, -77604, -77341, -77290, -77286, -77190, -76733, -76468, -76433, -76418, -76266, -76262, -76076, -75950, -75696, -75667, -75594, -75547, -75457, -75269, -75229, -75214, -75188, -75057, -74905, -74886, -74645, -74367, -74227, -74226, -74209, -74041, -73914, -73901, -73822, -73809, -73516, -73319, -73140, -73137, -73044, -73033, -72744, -72669, -72645, -72394, -72261, -72197, -71828, -71558, -71467, -71398, -71301, -71142, -71083, -70885, -70387, -70381, -70227, -70206, -70153, -70151, -69992, -69961, -69036, -68975, -68768, -68612, -68596, -68478, -68476, -68469, -68314, -68225, -67995, -67983, -67954, -67848, -67741, -67735, -67342, -66623, -66574, -66516, -66453, -66103, -66011, -65917, -65877, -65861, -65744, -65536, -65505, -65478, -65405, -65401, -65234, -64884, -64444, -64065, -63914, -63867, -63843, -63840, -63617, -63439, -63389, -63123, -62908, -62902, -62779, -62625, -62578, -62268, -61914, -61908, -61689, -61627, -61483, -61469, -61215, -61211, -61150, -61061, -60936, -60706, -60526, -60380, -60127, -60060, -59722, -59346, -59299, -59170, -58940, -58878, -58748, -58637, -58400, -58361, -58199, -57436, -56643, -56443, -56422, -56393, -56298, -55972, -55823, -55811, -55323, -55128, -54730, -53683, -53507, -53364, -52949, -52631, -52559, -52494, -51863, -51854, -51776, -51683, -51673, -51554, -51536, -51212, -51208, -51158, -50366, -50319, -50208, -49941, -49871, -49763, -49489, -49442, -49400, -49253, -48977, -48970, -48948, -48747, -48644, -48367, -48117, -48110, -47986, -47728, -47687, -46812, -46438, -46244, -46161, -46083, -46051, -46029, -46017, -46002, -45929, -45706, -45562, -45490, -45446, -45329, -45105, -45090, -44852, -44604, -44194, -44028, -43958, -43891, -43720, -43398, -43250, -42521, -42502, -42470, -42337, -42300, -42274, -42215, -42077, -41996, -41946, -41871, -41746, -41213, -41185, -40720, -40556, -40193, -39999, -39997, -39707, -39668, -39543, -39516, -39420, -39384, -39382, -39266, -38744, -38639, -38501, -38406, -38339, -37765, -37758, -37654, -37440, -37356, -37314, -37298, -37062, -36849, -36654, -36651, -36334, -36218, -36137, -35850, -35843, -35689, -35588, -35454, -35417, -35378, -35152, -35089, -35040, -34707, -34525, -34030, -33934, -33918, -33864, -33581, -33166, -32891, -32735, -32682, -32385, -32355, -32235, -32204, -32130, -31665, -31470, -31387, -31302, -31253, -31077, -30888, -30805, -30592, -30547, -30499, -30329, -30325, -30304, -30295, -30229, -29954, -29655, -29109, -29000, -28578, -28571, -28478, -28392, -28288, -28249, -28095, -28028, -27981, -27535, -27452, -27103, -26908, -26841, -26771, -26422, -26356, -26355, -26118, -26095, -26066, -26028, -25590, -25062, -24944, -24889, -24851, -24821, -24790, -24363, -24314, -24060, -24013, -23945, -23785, -23364, -23268, -23206, -23194, -23130, -22198, -22163, -21983, -21868, -21793, -21756, -21652, -21609, -21582, -21579, -21365, -21227, -21108, -21075, -20943, -20645, -20166, -19730, -19728, -19617, -19603, -19544, -19396, -19294, -19115, -18886, -18665, -18494, -18387, -18117, -17803, -17633, -17505, -17379, -17307, -17071, -16841, -16759, -16716, -16693, -16589, -16387, -16379, -16325, -16323, -16318, -16184, -16094, -15952, -15687, -15492, -15488, -15463, -15164, -15033, -14933, -14660, -13822, -13457, -13191, -12816, -12701, -12524, -12490, -11782, -11745, -11668, -11636, -10885, -10830, -10758, -10324, -10218, -10074, -10056, -9798, -9759, -9583, -9568, -9394, -9118, -9023, -8935, -8602, -8308, -8174, -7971, -7957, -7814, -7502, -7435, -7221, -7161, -6945, -6837, -6685, -6499, -6440, -6375, -6197, -6166, -5990, -5949, -5612, -5392, -5378, -5066, -5059, -5032, -4823, -4664, -4553, -4507, -4159, -3659, -3613, -3505, -3493, -3469, -3452, -3353, -3261, -3057, -3051, -2863, -2838, -2536, -2498, -2350, -2331, -2267, -2258, -2187, -1910, -1497, -1341, -1077, -887, -814, -757, -353, 40, 112, 348, 606, 659, 740, 992, 1515, 1538, 1729, 1749, 1823, 1877, 1913, 1990, 2177, 2265, 2382, 2512, 2528, 2580, 2666, 2669, 2727, 2749, 3005, 3028, 3066, 3916, 4044, 4249, 4375, 4582, 4619, 4960, 5035, 5106, 5893, 6058, 6233, 6246, 6974, 7207, 7271, 7788, 8255, 8366, 8370, 8408, 8460, 8521, 8599, 8819, 9058, 9158, 9483, 9604, 9641, 9762, 9790, 10004, 10027, 10142, 10186, 10363, 10462, 10567, 10631, 10901, 11049, 11392, 11663, 11787, 11797, 11955, 12230, 12460, 12633, 12871, 12928, 12936, 12970, 13001, 13105, 13596, 13889, 14579, 14811, 14889, 14949, 14994, 15063, 15123, 15143, 15202, 15246, 15333, 15841, 16036, 16068, 16121, 16237, 16367, 16582, 16587, 16682, 16871, 17122, 17306, 17449, 17769, 18069, 18073, 18194, 18214, 18219, 18220, 18228, 18425, 18580, 18842, 18915, 19096, 19300, 19647, 19792, 20033, 20483, 20736, 20833, 20944, 20966, 21000, 21157, 21168, 21184, 21698, 21723, 22028, 22117, 22153, 22286, 22342, 22364, 22420, 22813, 23017, 23179, 23371, 23390, 23647, 24267, 24346, 24503, 24664, 24725, 24727, 24894, 25077, 25108, 25461, 25563, 25769, 25867, 25889, 25940, 26304, 26359, 26519, 27088, 27651, 27868, 27885, 28278, 28523, 28659, 29068, 29222, 29289, 29324, 29327, 29462, 29599, 29618, 30141, 30518, 30613, 30944, 30952, 31187, 31255, 31299, 31626, 32002, 32156, 32212, 32410, 32465, 32811, 33087, 33222, 33230, 33473, 33509, 33643, 33708, 34421, 34741, 34888, 34913, 35154, 35223, 35370, 35440, 35725, 35772, 36161, 36243, 36251, 36271, 36297, 36316, 36497, 36713, 36794, 37433, 37681, 38032, 38257, 38310, 38349, 38817, 39121, 39135, 39694, 40347, 40421, 40595, 40610, 40642, 40814, 40890, 40983, 41021, 41130, 41235, 41448, 41491, 41542, 41612, 42011, 42154, 42195, 42217, 42308, 42759, 42886, 43103, 43260, 43286, 43381, 43430, 43530, 43550, 43610, 43662, 44738, 44815, 45408, 45450, 45559, 45657, 45660, 45715, 45762, 45913, 45932, 45950, 46009, 46197, 46261, 46299, 46308, 46310, 46349, 46522, 46570, 46692, 46753, 47028, 47169, 47292, 47302, 47449, 47606, 47859, 48088, 48474, 48937, 49362, 49551, 49682, 49868, 50122, 50132, 50138, 50436, 50518, 50568, 50684, 50883, 50974, 51117, 51144, 51352, 51410, 51465, 51898, 52017, 52177, 52195, 52226, 52260, 52325, 52447, 52832, 52906, 53356, 53418, 53808, 54098, 54350, 54373, 54462, 54669, 54814, 55335, 55407, 55445, 55658, 55665, 55710, 55728, 55765, 55825, 56230, 56367, 56405, 56520, 56533, 56820, 56829, 56910, 57469, 57517, 57817, 58257, 58512, 58519, 58632, 59368, 59384, 59580, 59902, 60214, 60262, 60494, 60761, 60950, 61046, 61107, 61203, 61689, 61714, 61783, 61870, 61927, 61951, 61982, 62688, 62726, 62860, 62922, 62958, 63067, 63172, 63280, 63303, 63352, 63541, 63580, 63614, 63681, 63836, 63991, 64050, 64187, 64298, 64302, 64622, 64704, 64727, 64856, 65049, 65159, 65293, 65337, 65370, 66264, 66301, 66694, 67224, 67297, 67384, 67842, 67877, 68036, 68211, 68253, 68271, 68416, 68650, 68689, 68930, 69054, 69106, 69726, 69783, 69906, 70244, 70332, 70369, 70508, 70637, 70716, 70776, 70945, 71201, 71778, 71897, 71950, 71987, 72006, 72134, 72301, 72362, 72479, 72622, 72790, 72996, 73191, 73341, 73395, 73426, 73491, 73497, 73534, 73749, 73846, 73889, 74341, 74484, 74517, 74661, 74889, 75789, 75824, 75939, 75997, 76075, 76111, 76430, 76514, 76648, 76802, 77122, 77179, 77371, 77406, 77506, 77648, 77780, 78025, 78212, 78371, 78392, 78544, 78602, 78749, 78933, 79057, 79239, 79447, 79580, 79804, 79858, 79938, 80035, 80146, 80449, 81070, 81267, 81495, 81930, 81931, 82001, 82418, 82617, 82630, 82754, 82860, 82937, 83047, 83080, 83499, 83649, 83819, 83941, 84126, 84464, 84727, 84952, 85075, 85251, 85716, 86147, 86231, 86327, 86363, 86635, 86791, 86892, 86893, 87043, 87342, 87390, 87435, 87495, 87501, 87511, 87754, 87978, 88150, 88181, 88235, 88575, 88687, 88936, 89474, 89480, 89960, 90297, 90365, 91040, 91149, 91234, 91251, 91544, 91569, 91692, 91693, 91728, 91741, 91928, 91956, 92011, 92120, 92994, 93128, 93393, 93415, 93487, 93896, 94254, 94315, 94335, 94441, 94543, 95096, 95100, 95205, 95236, 95320, 95448, 95625, 95935, 95981, 96114, 96158, 96300, 96359, 96397, 96420, 96729, 96790, 96799, 96926, 96965, 97018, 97068, 97300, 97641, 97678, 97744, 97854, 98002, 98079, 98134, 98178, 98463, 99049, 99158, 99457, 99846, 99857, 99886, 99933]
    random.shuffle(arr)
    arr_sorted = sorted(arr)
    bucket_sort(arr)
    assert arr == arr_sorted