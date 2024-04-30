# pyOCD debugger
# Copyright (c) 2023 Jon Suphammer
# Copyright (c) 2023 PyOCD Authors
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FLASH_ALGO = {
    'load_address' : 0x00200000,

    # Flash algorithm as a hex string
    'instructions': [
    0xe7fdbe00,
    0x0128f04f, 0x43416809, 0xfbb12003, 0x2801f0f0, 0x1e80d902, 0xd2fd1e40, 0x00004770, 0x4770ba40,
    0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770bac0,
    0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x0030ea4f,
    0x00004770, 0x0030ea4f, 0x00004770, 0x0030ea4f, 0x00004770, 0x0030ea4f, 0x00004770, 0x0030ea4f,
    0x00004770, 0x0030ea4f, 0x00004770, 0x0030ea4f, 0x00004770, 0x0030ea4f, 0x00004770, 0xf001b510,
    0x485ffdae, 0x5140f44f, 0x4c5e6a42, 0x6062444c, 0x4a5d6809, 0x6a414291, 0xf441d102, 0xe0016180,
    0x6180f421, 0xf0016241, 0xa058fdca, 0xfdc8f001, 0xfcc6f001, 0xfefcf000, 0xfff7f000, 0xa156b108,
    0xa157e000, 0xf001a058, 0xf000fdbb, 0x4601fcbd, 0xf001a059, 0x484bfdb5, 0xf0014448, 0xb2c1f979,
    0xa0597822, 0xfdacf001, 0xf0012000, 0x4601f991, 0xf001a05b, 0x2000fda5, 0xb538bd10, 0x49404c41,
    0x6860444c, 0xa05a6248, 0xfd9af001, 0xa05b7821, 0xfd96f001, 0xf0017820, 0x4605f97b, 0xa05c4601,
    0xfd8ef001, 0xd0052d01, 0xa05c7821, 0xfd88f001, 0xbd382001, 0xf88d2000, 0x46680000, 0xf948f001,
    0x1000f89d, 0xf001a05b, 0x2000fd7b, 0xb510bd38, 0xf001a05e, 0x2100fd75, 0xf0002001, 0x2000fff2,
    0xb570bd10, 0x46014605, 0xf001a05c, 0xf001fd69, 0xb188f917, 0x74c0f04f, 0x0000f44f, 0xd20042a5,
    0xf0014604, 0x1901f90d, 0x5080f505, 0xd3074281, 0xa0524629, 0xfd54f001, 0x20024629, 0xffd1f000,
    0xbd702000, 0x4615b570, 0x46024604, 0xa04e460e, 0xfd46f001, 0x4631462a, 0xf0014620, 0x2000f8ca,
    0xb5f0bd70, 0x4616b0bd, 0x4607460c, 0x2cf0e012, 0x25f0d901, 0x4625e000, 0x4629466a, 0xf0004638,
    0x462afd69, 0x46304669, 0xf977f002, 0x442fb920, 0x1b64442e, 0xdcea2c00, 0x4638b03d, 0x0000bdf0,
    0x40006000, 0x00000004, 0xd10342ac, 0x74696e49, 0x0a2e2e2e, 0x00000000, 0x65757254, 0x00000000,
    0x736c6146, 0x00000065, 0x5f797271, 0x6f666e69, 0x25203d20, 0x00000073, 0x73616c66, 0x78655f68,
    0x3a747369, 0x00582520, 0x20746572, 0x6425203d, 0x7062202c, 0x6c766c5f, 0x25203d20, 0x00000064,
    0x20746573, 0x20746572, 0x7825203d, 0x00000000, 0x6e496e55, 0x2e2e7469, 0x00000a2e, 0x20746553,
    0x4c205042, 0x6c657665, 0x2e642520, 0x00002e2e, 0x20746572, 0x6425203d, 0x00000000, 0x20746553,
    0x4c205042, 0x6c657665, 0x20642520, 0x6c696166, 0x0000002e, 0x20746553, 0x4c205042, 0x6c657665,
    0x20642520, 0x6b636162, 0x0000002e, 0x70696843, 0x61724520, 0x2e2e6573, 0x00000a2e, 0x73617245,
    0x20676e69, 0x000a7825, 0x676f7250, 0x6d6d6172, 0x20642520, 0x65747962, 0x6f742073, 0x0a702520,
    0x00000000, 0x20000041, 0xbf00e00a, 0xbf00bf00, 0xbf00bf00, 0xbf00bf00, 0xbf00bf00, 0x1c40bf00,
    0xd3f24288, 0xb5004770, 0x20012200, 0xffeaf7ff, 0xf44f48fe, 0x4611737a, 0x42991c52, 0x49fcd305,
    0x44492002, 0x20007048, 0x6a81bd00, 0xd00207c9, 0x06896a81, 0x2001d5ef, 0xffd4f7ff, 0xbd002001,
    0x220148f4, 0x23034448, 0x2f08f820, 0xf02178c1, 0x70c10101, 0x77c12100, 0x71417101, 0x23027183,
    0x23bb7243, 0x233b7203, 0x760171c3, 0x72c3239f, 0x72832306, 0x23057701, 0x73427303, 0x21607781,
    0x21d87381, 0x212073c1, 0x21ab7401, 0x21b97441, 0x21667481, 0x219974c1, 0x21327501, 0x21eb76c1,
    0x216b7681, 0x21357641, 0x47707741, 0x4ad9b5f0, 0x444a2406, 0xf8822500, 0x7ad14020, 0x0711f642,
    0x0301f021, 0x213872d3, 0x1023f882, 0x26151bc1, 0x5025f882, 0xd02842b8, 0xf1a0dc0b, 0xf5b00016,
    0xd01b5000, 0xd0192801, 0x7000f5a0, 0xd10638fe, 0x2901e01b, 0x2903d019, 0x2905d017, 0x49c4d015,
    0x4449200c, 0x88107048, 0x2007f3c0, 0xd1042828, 0x0004f023, 0x0002f040, 0xbdf072d0, 0x741020bb,
    0x4020f882, 0x6027f882, 0xf882e7ed, 0x76556027, 0x49b8e7e9, 0x4449b510, 0xf8812209, 0x7aca2020,
    0xf0422350, 0x72ca0201, 0x3024f881, 0x0416f246, 0x42a01b03, 0xdc0dd00d, 0x0016f1a0, 0x0231f04f,
    0x4080f5b0, 0x2801d015, 0x1c40d013, 0x5f00f5b0, 0xbd10d10a, 0xf5b32000, 0xd00d7f7f, 0x7340f5a3,
    0xd0093bfd, 0xd0122b01, 0x200c49a1, 0x70484449, 0xf881bd10, 0xbd102026, 0x0020f881, 0x0201f022,
    0x2f0bf801, 0x75c87608, 0x71487588, 0x7408e009, 0x0020f881, 0x0201f022, 0x2f0bf801, 0x75c87608,
    0x76887588, 0xbd107648, 0x38124992, 0x7aca4449, 0x0201f042, 0x220972ca, 0x2020f881, 0xf8812250,
    0xf5b02024, 0xd00640c0, 0xd0042802, 0x200c4988, 0x70484449, 0x20314770, 0x0026f881, 0xb5304770,
    0x21ff4b84, 0x2250444b, 0x1020f883, 0xf6437ad9, 0xf0210513, 0x72d90101, 0x2024f883, 0x24001b42,
    0xd01a42a8, 0xf600dc0b, 0xf5b070ec, 0xd0134080, 0x60e0f5a0, 0xd01038fd, 0xd1092801, 0x2a02e00d,
    0xf202d00a, 0xf5b272fe, 0xd0054280, 0xd00c2a01, 0x200c496f, 0x70484449, 0xf021bd30, 0xf8030001,
    0x765c0f0b, 0x769c759c, 0xf803bd30, 0x711c4f21, 0x4968bd30, 0x44492209, 0xf8813813, 0xf8112020,
    0xf0422f0b, 0x700a0201, 0x764a2250, 0x4080f5b0, 0x2801d007, 0x2802d005, 0x495dd003, 0x4449200c,
    0x47707048, 0xb510495b, 0x23094449, 0xf2447aca, 0xf0420418, 0x72ca0201, 0x3020f881, 0xf8812350,
    0x1b033024, 0xdd0e42a0, 0x0306f103, 0x5f00f5b3, 0xf022d109, 0xf8010001, 0x20000f0b, 0x76087548,
    0x758875c8, 0xbd107688, 0x2106484a, 0xf8804448, 0xf8101020, 0xf0411f0b, 0x70010101, 0x76812148,
    0x76c12142, 0x48434770, 0xf8104448, 0xf0411f0b, 0x70010101, 0x75412109, 0x76412150, 0x483d4770,
    0xf8104448, 0xf0411f0b, 0x70010101, 0x7541210a, 0x76412150, 0x76c12131, 0x48364770, 0xf8104448,
    0xf0411f0b, 0x70010101, 0x75412109, 0x76412150, 0x76c12131, 0x492f4770, 0x50ecf600, 0xf5b04449,
    0xd00f4080, 0x6060f5a0, 0xd10a3804, 0x0f0bf811, 0x0001f040, 0x20097008, 0x20507548, 0x20317648,
    0x477076c8, 0xf8012000, 0x74c80f10, 0x74487488, 0x47707548, 0x4ff7e92d, 0x46154e1c, 0xf8d6460c,
    0x2701b11c, 0xa000f8d6, 0x8004f8d6, 0x60b02000, 0xf9c5f001, 0xf4406830, 0x60307040, 0x20006074,
    0xf0019900, 0x4813f9c2, 0x7b404448, 0xf9d7f001, 0x60b02001, 0xfe17f7ff, 0x2700b900, 0x60b02000,
    0xe007b92f, 0xf0012000, 0xf805f9bd, 0x1e640b01, 0xd2f7b2e4, 0x00fff00b, 0xf9c1f001, 0xa000f8c6,
    0xf088fa1f, 0x46386070, 0x8ffee8bd, 0x40080000, 0x0000000f, 0x0000003c, 0x48fcb5f8, 0x44484dfc,
    0x20007d06, 0x0000f88d, 0xe00a4604, 0x2101466a, 0xf7ff4630, 0x2800ffaf, 0xf89dd00c, 0x07c00000,
    0x4620d009, 0x42a81c64, 0x49f2d9f0, 0x44492003, 0x20007048, 0x2001bdf8, 0xe92dbdf8, 0x4fee4df0,
    0x460c4615, 0xb000f8d7, 0x26014680, 0xa118f8d7, 0x60b82000, 0xf963f001, 0xf9a8f001, 0x4118f8c7,
    0xe0014641, 0x1b01f815, 0xf0012000, 0x1e64f95e, 0xd2f7b2e4, 0x60b82001, 0xfdb5f7ff, 0x2600b900,
    0x60b82000, 0x0fb9f1b8, 0xf1b8d007, 0xd0040f50, 0xf7ffb11e, 0xb900ffb1, 0xf8c72600, 0xf8c7b000,
    0x4630a118, 0x8df0e8bd, 0x48d0b5f8, 0x44482400, 0x7d064622, 0x46217c80, 0xffbff7ff, 0xd0122800,
    0x46204dcb, 0x42a81c64, 0x466ad80e, 0x46302101, 0xff50f7ff, 0xd0062800, 0x1000f89d, 0xd1f007c8,
    0xd5ee0788, 0xbdf82001, 0x200549c2, 0x70484449, 0xbdf82000, 0xb51048bd, 0xf8904448, 0xb1200024,
    0x46112200, 0xff99f7ff, 0xf7ffe001, 0x2800ffcd, 0x2001d000, 0xe92dbd10, 0x4fb445f8, 0x444f4688,
    0x0a04b2c5, 0x7d382600, 0x2101466a, 0xff22f7ff, 0xd04e2800, 0x2601b155, 0x0000f89d, 0x0f01f1b8,
    0x4228d01e, 0x43a8d044, 0x0000f88d, 0xb30c46ea, 0x07c07af8, 0x2602d01e, 0x0025f897, 0xf10a2101,
    0xf7ff0201, 0x2800ff07, 0xf89dd033, 0xf1b80001, 0xd00a0f01, 0xd02b4220, 0xf88d43a0, 0xe00a0001,
    0x0100ea35, 0x4328d024, 0xea34e7de, 0xd01f0100, 0xe7f24320, 0xf897b1e6, 0xb1e00026, 0xf7ffb155,
    0x2800ffa9, 0x7d78d015, 0x2101466a, 0xff45f7ff, 0xd00e2800, 0xf7ffb164, 0x2800ff9d, 0xf897d009,
    0xf10a0026, 0x21010201, 0xff37f7ff, 0xd0002800, 0xe8bd2001, 0xf7ff85f8, 0x2800ff8d, 0x7d78d0f9,
    0x4631466a, 0xb5f8e7f0, 0x46144d80, 0x444d460e, 0x7d2bb138, 0x21014602, 0xf7ff4618, 0x2800febb,
    0x27ffd01f, 0xf895b16e, 0xb9100025, 0x0027f895, 0x4632b130, 0xf7ff2101, 0x2800fead, 0xe000d011,
    0xb16c7037, 0x0027f895, 0x466ab148, 0xf7ff2102, 0x2800fea1, 0xf89dd005, 0x70200001, 0x7027e000,
    0xbdf82001, 0x43f8e92d, 0xa06c4606, 0x0400f04f, 0xf8df6800, 0x46178198, 0x9000000d, 0x46224621,
    0x44c84668, 0xf898d102, 0xb9033026, 0xb1071c41, 0x46681c82, 0xffb7f7ff, 0xd01d2800, 0x0026f898,
    0xb15eb1e0, 0xff36f7ff, 0xd0152800, 0x0015f898, 0x21014632, 0xfed1f7ff, 0xd00d2800, 0xf7ffb15d,
    0x2800ff29, 0xf898d008, 0x462a0026, 0xf7ff2101, 0x2800fec4, 0x2001d000, 0x83f8e8bd, 0x7830b11e,
    0xf88d2401, 0xb1250000, 0x24027828, 0x0001f88d, 0xf89de005, 0xb1100001, 0xd00028ff, 0xb1272402,
    0x24037838, 0x0002f88d, 0xf89de005, 0xb1100002, 0xd00028ff, 0xf7ff2403, 0x2800fefd, 0xf898d0dc,
    0x466a0015, 0xe7d24621, 0x4448483a, 0x78401ec0, 0x49384770, 0x1ec94449, 0x4302784a, 0x4770704a,
    0x44484832, 0x47706800, 0x2000b570, 0xf820f001, 0x20004c31, 0x4d2d60a0, 0x444d34a4, 0xf0018928,
    0x2004f81c, 0x0ca0f844, 0xf36f6fa0, 0x67a00011, 0xf4406fa0, 0x67a03040, 0xf0017b28, 0x6868f800,
    0x200167e0, 0x0c9cf844, 0xe92dbd70, 0xf8df47f0, 0x46068088, 0x64c0f44f, 0x0120f8d8, 0x3580f3c0,
    0xf8c82000, 0x4f190008, 0x8938444f, 0xfff5f000, 0xf44fb10d, 0x2004448c, 0x0004f8c8, 0x011cf8d8,
    0x0011f36f, 0x011cf8c8, 0x011cf8d8, 0x3040f440, 0x011cf8c8, 0xf8c87c78, 0x7af800f4, 0xf0202e02,
    0x72f80080, 0x2e01d003, 0xb396d043, 0xb12de079, 0x111cf8d8, 0x1180f441, 0x111cf8c8, 0x1023f897,
    0x2938b1d1, 0x2932d00c, 0xe012d00f, 0x0000003c, 0x00b71b00, 0x0000000f, 0x40080000, 0x00ffffff,
    0x7480f444, 0x1104f8c8, 0xf044e003, 0xf8c80480, 0xf0401100, 0x72f80080, 0x0022f897, 0xf044b150,
    0xf8c80410, 0x72b800f0, 0xf0207af8, 0x30100018, 0xe02de00b, 0x0021f897, 0xf044b3d8, 0xf8c80408,
    0x72b800ec, 0xf0207af8, 0xf0200018, 0x30400060, 0xb12de036, 0x111cf8d8, 0x1100f441, 0x111cf8c8,
    0xb1417c39, 0x0404f044, 0x10e8f8c8, 0x0018f020, 0x300872b9, 0x7bf9e008, 0xf044b1d9, 0xf8c80402,
    0x72b910e4, 0x0018f020, 0x0060f020, 0xe0173020, 0xf8d8b12d, 0xf441111c, 0xf8c80180, 0x49fe111c,
    0x44494afe, 0x42916889, 0xf044d304, 0x210b0401, 0xe006e003, 0xf0247bb9, 0x72b90401, 0x0078f020,
    0xf8d872f8, 0xf0400110, 0xf8c80001, 0xf8d80110, 0xf0200110, 0xf8c80002, 0xf8970110, 0xb1880020,
    0xd00f28ff, 0x25082101, 0xa3acf8df, 0x44ca2e02, 0xf100fa01, 0x0a03f10a, 0xd00bb288, 0xf7ff2100,
    0xb148fe0a, 0x4120f8c8, 0x607c2001, 0x0008f8c8, 0x87f0e8bd, 0xe7f22101, 0x5001f88a, 0xe7f72000,
    0x49dfb538, 0x511cf8d1, 0x60882000, 0xff20f000, 0xf0002000, 0x48dbff14, 0x4448466a, 0x7cc02103,
    0xfd18f7ff, 0xf89db170, 0xf89d0000, 0x04001001, 0x2401ea40, 0x0002f89d, 0xb2e84304, 0xfefff000,
    0xbd384620, 0xbd3848d0, 0x0f00f5b0, 0xf5a0d301, 0x47700000, 0x41f0e92d, 0x460c4616, 0xfff4f7ff,
    0xe00e4607, 0xd9012c3c, 0xe000253c, 0x46324625, 0x46384629, 0xff10f000, 0xd0052800, 0x442e442f,
    0x2c001b64, 0x2001dcee, 0x81f0e8bd, 0x45f8e92d, 0x48b94eb9, 0x4448444e, 0x300c78b1, 0xf8102700,
    0xf8df4011, 0x4db6a2e8, 0x82dcf8df, 0xe0289700, 0x60a82000, 0xf0004620, 0x2001fec2, 0x466a60a8,
    0x46502104, 0xffc6f7ff, 0x45419900, 0x49add117, 0x44492701, 0x78b0730c, 0x2000b9b0, 0xf8d560a8,
    0xf020011c, 0xf8c5707f, 0xf8d5011c, 0xea40011c, 0xf8c54084, 0x2001011c, 0x734c60a8, 0x1c64e004,
    0x7830b2e4, 0xd3d34284, 0xe5d24638, 0x4e9db5f8, 0x444e4604, 0x07807af0, 0x4997d406, 0x44492007,
    0x70481cc9, 0xbdf82000, 0x5027f896, 0x2000b38d, 0x7d309000, 0x2101466a, 0xfc8cf7ff, 0x0703f06f,
    0x2102b348, 0xf10d4628, 0xf7ff0201, 0xb310fc83, 0xd0022c01, 0xd004b154, 0xf89de00c, 0x07800002,
    0xf89dd417, 0xf0400002, 0xe0070002, 0x0002f89d, 0xd50e0780, 0x0002f89d, 0x0002f020, 0x0002f88d,
    0xfd28f7ff, 0x7d70b138, 0x2103466a, 0xfcc5f7ff, 0x2001b108, 0x4638bdf8, 0x497abdf8, 0x81084449,
    0xb5104770, 0x4a744877, 0x444a4448, 0x24016800, 0x4107f3c0, 0xb2807853, 0xb1531cd2, 0xd03d2968,
    0x2920dc11, 0xdc09d031, 0xd02b290b, 0xd116291c, 0x200ae022, 0xf04f7050, 0xbd1030ff, 0xd0302952,
    0xd10c295e, 0x29c2e027, 0xdc04d00d, 0xd01f2985, 0xd10429a1, 0x29c8e013, 0x29efd008, 0x200bd009,
    0x24007050, 0xf7ffe022, 0xe01cfab1, 0xfaf1f7ff, 0xf7ffe019, 0xe016fb39, 0xfb51f7ff, 0xf7ffe013,
    0xe010fb88, 0xfb9ef7ff, 0xf7ffe00d, 0xe00afbbd, 0xfbc9f7ff, 0xf7ffe007, 0xe004fbee, 0xfbddf7ff,
    0xf7ffe001, 0x2002fbcc, 0xfdd3f7ff, 0xbd104620, 0x47f0e92d, 0xf04f4e48, 0x444e30ff, 0x78711cf4,
    0xf7ffb139, 0x4605ff9e, 0xd0052801, 0x70602011, 0x2110e035, 0xe6bb7061, 0x27124842, 0xf06f4448,
    0x7b400a03, 0xf896b948, 0x20008002, 0xfdddf7ff, 0xf7ffb368, 0xf886fefb, 0x78b08002, 0xfdd5f7ff,
    0xf7ffb328, 0xb1e0fef3, 0xf8d24a35, 0xf3c00120, 0xb1a03080, 0x011cf8d2, 0x78b3492f, 0x310c4449,
    0x000bf3c0, 0x1013f831, 0xd8084281, 0x311cf8d2, 0xf0001a40, 0xea43000f, 0xf8c23000, 0x4628011c,
    0x2000e686, 0xfdb1f7ff, 0x2500b108, 0x7067e7f7, 0xe67d4650, 0x4000ea41, 0xf0400040, 0xf04f0001,
    0xf0204280, 0x64910101, 0x64916490, 0xf04f4770, 0x04404180, 0x6c886488, 0x2047f3c0, 0xe92d4770,
    0x250047f0, 0xf0004628, 0xf8dffd93, 0x20008054, 0x0008f8c8, 0xfd63f000, 0xfda8f000, 0xa038f8df,
    0xf10a44ca, 0xeb050a12, 0x465207c5, 0x0007f81a, 0xd04007c1, 0x0041f3c0, 0xf8c84643, 0x18be0118,
    0x0001f8b6, 0xeb00b120, 0x00400080, 0xf99af7ff, 0x46982400, 0xe00b4692, 0x0000000c, 0x03f83c40,
    0x40080000, 0x0000003c, 0x5a5a12a5, 0x00804030, 0x0007f81a, 0x00c3f3c0, 0x07c040e0, 0x1930d00f,
    0x20007941, 0xfd31f000, 0xf8c82001, 0xf7ff0008, 0x2800f98a, 0x0000f04f, 0x0008f8c8, 0x1c64d011,
    0x2c04b2e4, 0xf8b6d3d7, 0xb1200003, 0x0080eb00, 0xf7ff0040, 0x1c6df967, 0x2d02b2ed, 0x2001d3b3,
    0x2000e606, 0x49fde604, 0x2000b510, 0xf7ff62c8, 0xf7fff987, 0x4cfaff94, 0xb138444c, 0xfe00f7ff,
    0x428849f8, 0x2004d104, 0xe01c7060, 0xe7fb2001, 0x49f5b1c8, 0x44490c02, 0x83c8774a, 0x49f36008,
    0xd1074288, 0xf7ffb280, 0x2000f9a1, 0xfe6ef7ff, 0xd1082801, 0xf7ff2000, 0xb120fd08, 0xf7ff2001,
    0x2001fcd8, 0x2000bd10, 0xe92dbd10, 0x48e641f0, 0x44482400, 0x48e26805, 0x4c07f3c5, 0x1ec04448,
    0x7840b2ae, 0xd3012804, 0xe60d2001, 0xd1072801, 0xfe97f7ff, 0xd0032801, 0xf000a0dd, 0xe02efdb1,
    0x21334fe5, 0xf04f447f, 0xeb047280, 0xeb070044, 0x78430080, 0xd11a4563, 0x42b38843, 0x6840d117,
    0xd8144290, 0xf000a0dd, 0x49cffd9b, 0x0044eb04, 0x312c4449, 0x0280eb07, 0x2000230c, 0x540c5c14,
    0x42981c40, 0x2004dbfa, 0xfc93f7ff, 0x1c64e7cc, 0x428cb2a4, 0x4629d3d9, 0xf000a0d6, 0x2000fd81,
    0xe92de5d2, 0xb0844df3, 0xf04f4607, 0x46550a00, 0xf7ff9805, 0x0c01fda9, 0x1008f88d, 0xf88d0a01,
    0xf88d1009, 0x2000000a, 0x46049000, 0x90014606, 0xb2d4f8df, 0x44cb9805, 0x0801f100, 0x2d01e049,
    0x462ad906, 0x9905a0cc, 0xfd5af000, 0xff8df7ff, 0xfb2af7ff, 0x2f01b3e8, 0x2f04d004, 0x2f02d00b,
    0xe01fd013, 0xf8db2400, 0xf89b6030, 0x46220016, 0x1f364621, 0xea4fe013, 0xea4f4418, 0xf64f4404,
    0x182670fc, 0x0017f89b, 0xea4fe007, 0xea4f3418, 0xf89b3404, 0xf6040018, 0xaa0276fc, 0xf7ff2103,
    0xb1b0facc, 0x46214632, 0xf000a0bd, 0x466afd29, 0x46202104, 0xfd5ef7ff, 0x2104aa01, 0xf7ff4630,
    0x9800fd59, 0xd1021c40, 0x1c409801, 0xf04fd00a, 0x46280a00, 0xb2ed1c6d, 0xd3b0280a, 0x4650b006,
    0x8df0e8bd, 0x0a01f04f, 0xb570e7f8, 0x20002401, 0xfc3ef000, 0x20004d81, 0xf00060a8, 0xf000fc10,
    0x2000fc55, 0x0118f8c5, 0x4449497f, 0xf0007e49, 0x2001fc0c, 0xf7ff60a8, 0xb900f866, 0x20002400,
    0x462060a8, 0xb510bd70, 0xf7ff4604, 0x2800ffde, 0x2c01d00b, 0x4874d108, 0x44482200, 0x7e804611,
    0xfa7bf7ff, 0xd0002800, 0xbd102001, 0x438a6802, 0x47706002, 0xd1014208, 0x47702001, 0x47702000,
    0x4ff7e92d, 0xa1a0f8df, 0x44ca2501, 0xf89a2700, 0x46164023, 0x293c4688, 0xb1ded81c, 0xfa94f7ff,
    0xd0182800, 0xb174f8df, 0xf8cb2000, 0x20030008, 0x0118f8cb, 0x000bf89a, 0xd4020600, 0x4011f89a,
    0x98002701, 0x4304ba00, 0xfc00f000, 0xf000b12f, 0xe00ffbb6, 0xe8bd2000, 0xf89a8ffe, 0x28380023,
    0x2832d002, 0xe005d002, 0xe0002102, 0x20022100, 0xfbddf000, 0x20024621, 0xfba7f000, 0xe0052400,
    0x20005d31, 0xfba1f000, 0xb2e41c64, 0xd3f74544, 0x465c2001, 0x0008f8cb, 0xfff5f7fe, 0xb115b138,
    0xf9faf7ff, 0x2000b118, 0x462860a0, 0x2500e7d3, 0xe92de7f9, 0x461741f0, 0xf7ff460d, 0x4606fca5,
    0xf106e017, 0x0a00003c, 0x2f16ebb0, 0xb2f0d903, 0x7480f5c0, 0x243ce000, 0xd90042ac, 0x463a462c,
    0x46304621, 0xff8cf7ff, 0xd0052800, 0x44274426, 0x2d001b2d, 0x2001dce5, 0x4928e4a6, 0x47706088,
    0xb5104827, 0x1ec04448, 0x28047840, 0x4826d303, 0x6b004448, 0xf7ffbd10, 0x06c1fc53, 0xf000d506,
    0xf44f010f, 0x1e493000, 0xbd104088, 0xbd102000, 0x4605b538, 0x4448481a, 0x78401ec0, 0xf04f2804,
    0xd3110000, 0xf88d4c18, 0x444c0000, 0x7d20466a, 0xf7ff2101, 0xb140f95f, 0x0035f894, 0x1000f89d,
    0x0091ea00, 0x20017028, 0xf06fbd38, 0xbd380003, 0xb086b570, 0x20004604, 0x0010f88d, 0x44484808,
    0x78401ec0, 0xd3052804, 0x444d4d07, 0x0034f895, 0xd26142a0, 0xb0062000, 0xe05dbd70, 0x40080000,
    0x0000000f, 0x5a5a12a5, 0x0000003c, 0x00c22814, 0x64616f6c, 0x76646120, 0x6766635f, 0x20666920,
    0x20746f6e, 0x6461656c, 0x79206465, 0x66207465, 0x2e6c6961, 0x00002e2e, 0x0000144c, 0x646e6946,
    0x65757120, 0x695f7972, 0x206f666e, 0x52206e69, 0x00214d4f, 0x72657571, 0x6e695f79, 0x6e206f66,
    0x6620746f, 0x646e756f, 0x44522021, 0x3d204449, 0x25783020, 0x002e786c, 0x73617245, 0x61662065,
    0x21216c69, 0x64646120, 0x78303d72, 0x78383025, 0x6572202c, 0x20797274, 0x2e2e6425, 0x0000002e,
    0x72617473, 0x25203a74, 0x2c583830, 0x646e6520, 0x3025203a, 0x00005838, 0x102cf895, 0xd00229ff,
    0xd003297f, 0xb134e007, 0xe0044604, 0x42a0b11c, 0x1e42d001, 0xf895b2d4, 0x6b2b2035, 0x3000e9cd,
    0x8deb9202, 0x202df895, 0x447848fe, 0xfb88f000, 0xf7ffa804, 0x2801ff4d, 0xf89dd109, 0x42a00010,
    0xf44fd105, 0xa0f8612b, 0xfb7af000, 0xa903e01a, 0xa803460a, 0x1c921c41, 0xf9e5f7ff, 0x0603f06f,
    0xf89db190, 0xf895100c, 0x22000035, 0x0180ea21, 0xea414020, 0xf88d0080, 0x4611000c, 0xf7ffa803,
    0xb108fa01, 0xe7562001, 0xe7544630, 0x4604b5f8, 0x444848e8, 0x28047840, 0x4ee7d31c, 0xf896444e,
    0x28ff002c, 0x287fd00c, 0xf06fd00a, 0x28080503, 0x4631d91f, 0x7027f896, 0x3025f891, 0xe002b117,
    0xe0262001, 0x3808b133, 0xb12fb2c6, 0x2101466a, 0xe0054638, 0xbdf82000, 0x466ab14b, 0x46182101,
    0xf868f7ff, 0xf89db1b8, 0x40f00000, 0x2001e00f, 0x2000bdf8, 0x0000f88d, 0x466a7d30, 0xf7ff2101,
    0xb140f859, 0x102cf896, 0x0000f89d, 0xf00040c8, 0x70200001, 0x4628e7eb, 0xe92dbdf8, 0x460547fc,
    0xf88d2000, 0x1e440004, 0x444848c2, 0x28047840, 0x2400d201, 0xa801e067, 0xffa8f7ff, 0xd1032801,
    0x0004f89d, 0xd05d42a8, 0x444f4fbb, 0x002cf897, 0xd05728ff, 0xd055287f, 0x0a01f04f, 0x0603f06f,
    0x28084669, 0x3808d924, 0xb2c74688, 0x46402200, 0xf7ff1c49, 0xb3e8f958, 0x0001f89d, 0xf107fa0a,
    0xfa054388, 0x4308f107, 0x0001f88d, 0xf1082200, 0x46100101, 0xf976f7ff, 0x2200b360, 0x0101f108,
    0xf7ff4668, 0xb328f940, 0x0001f89d, 0xe02540f8, 0x4668460a, 0x1c921c49, 0xf935f7ff, 0xf897b1d0,
    0xf89d002c, 0xfa0a1000, 0x4391f200, 0xf000fa05, 0xf88d4301, 0x22001000, 0x46684611, 0xf952f7ff,
    0x2200b140, 0x46684611, 0xf91df7ff, 0xf89db110, 0xe0000000, 0xf897e00a, 0x40c8102c, 0x0001f000,
    0xd10042a8, 0x46202401, 0x87fce8bd, 0xe7fa4634, 0x4605b5f8, 0x460f4887, 0x78404448, 0xf04f2804,
    0xd30e0000, 0xf88d4e84, 0x444e0000, 0x6b302400, 0x0f00f5b5, 0x0000f500, 0x4285d301, 0xf06fd902,
    0xbdf80002, 0x466a7d30, 0xf7fe2101, 0xb320ffb3, 0x0035f896, 0x1000f89d, 0x0091ea10, 0xd01a7038,
    0x102cf896, 0xd01329ff, 0x46044a74, 0x1e64447a, 0xeb02b2e4, 0xf8520184, 0x68490024, 0x0000f500,
    0x0100f501, 0xd3014285, 0xd301428d, 0xd1ee2c00, 0xf7ff4620, 0x2001fe3d, 0xf06fbdf8, 0xbdf80003,
    0x20ff4964, 0x78494449, 0xd3032904, 0x44484862, 0x0034f890, 0x49604770, 0x310e4449, 0x47706001,
    0x4449495d, 0x60013120, 0x495b4770, 0x312c4449, 0x47706001, 0x4e58b5f8, 0x444e2300, 0x7af0461c,
    0xf3c025ff, 0xf3c001c1, 0xf8961241, 0xb1580023, 0xf8d04853, 0x05f66120, 0x2302d501, 0xf8d0e003,
    0x06000120, 0x2402d500, 0x0004ea52, 0x2a01d004, 0x2a02d004, 0xe007d005, 0xe0052500, 0x2501b924,
    0x2c02e002, 0x2502d100, 0x9400a046, 0xfa08f000, 0xbdf84628, 0x4c42b570, 0x60a02000, 0xf90ff000,
    0xf954f000, 0xf8c42000, 0x4d3b0118, 0x7ee9444d, 0xf90bf000, 0x60a02001, 0xfd65f7fe, 0x2000b180,
    0xf00060a0, 0x7f29f943, 0xf0002000, 0x2001f8fe, 0xf7fe60a0, 0xb118fd58, 0x60a02000, 0xe5db2001,
    0x60a02000, 0x4770e5d8, 0x4180f04f, 0x2801b1b0, 0x2802d019, 0xf8d1d111, 0xf02002a8, 0xf8c16000,
    0xf8d102a8, 0xf04002a8, 0xf8c16080, 0xf8d102a8, 0xf02002a8, 0xf8c17080, 0x477002a8, 0x02a8f8d1,
    0x6000f020, 0xf8d1e003, 0xf04002a8, 0xf8c16000, 0xf8d102a8, 0xf02002a8, 0xf8c16080, 0xf8d102a8,
    0xf04002a8, 0xe7e67080, 0x2500b57c, 0xb120462c, 0xd0502801, 0xd16e2802, 0x20f62501, 0xfdaaf000,
    0x20f74606, 0xfda6f000, 0xf0264601, 0xf0210040, 0xf0400112, 0xf0410023, 0x46010609, 0xf00020f6,
    0xe023fda5, 0x0000132e, 0x656e696c, 0x6425203a, 0x00000000, 0x0000000c, 0x0000003c, 0x00001028,
    0x40080000, 0x635f6472, 0x64253d68, 0x6472202c, 0x3d61645f, 0x202c6425, 0x635f7277, 0x64253d68,
    0x7277202c, 0x3d61645f, 0x00006425, 0x20f74631, 0xfd7cf000, 0x94002301, 0x2100461a, 0x9401200b,
    0xfc0ff000, 0x94002301, 0x2100461a, 0x9401200c, 0xfc07f000, 0x2301b1fd, 0x461a9400, 0x20144619,
    0xf0009401, 0x2201fbfe, 0x23009400, 0x20154611, 0xf0009401, 0x2301fbf6, 0x461a9400, 0x20164619,
    0xf0009401, 0x2301fbee, 0x461a9400, 0x20174619, 0xf0009401, 0xe8bdfbe6, 0x2064407c, 0xbc92f7fe,
    0x4604b510, 0xff80f7ff, 0xe8bd4620, 0xe74b4010, 0xf04fb510, 0xf8d44480, 0xf040020c, 0xf8c40020,
    0x2201020c, 0x2010495c, 0x740bf504, 0xfa0cf000, 0xf0406fe0, 0x67e07080, 0xf0406fe0, 0x67e07000,
    0xf00020f6, 0xf040fd17, 0x20f60101, 0xfd2ff000, 0xfb09f7ff, 0x68084951, 0x0001f020, 0xbd106008,
    0xf04fb510, 0xf8d04080, 0xf041120c, 0xf8c00110, 0x2000120c, 0xffc4f7ff, 0x4010e8bd, 0x4848e7c8,
    0xf4216801, 0x6001117c, 0x4a454770, 0xd0042801, 0xd0052802, 0x1060f882, 0xf8a24770, 0x47701060,
    0x47706611, 0x2801493e, 0x2802d004, 0xf891d005, 0x47700060, 0x0060f8b1, 0x6e084770, 0x4a384770,
    0x111cf8d2, 0x010ff36f, 0xf8c24301, 0x4770111c, 0x40812101, 0x61014832, 0x1e414770, 0x72fff64e,
    0xd2034291, 0xf3c0492e, 0x6148000b, 0x4a2c4770, 0xf4236813, 0x6013137c, 0x0b890789, 0x0003f000,
    0x4080ea41, 0x43086811, 0x47706010, 0x68014824, 0x7140f421, 0x47706001, 0x4df0e92d, 0x4921460d,
    0x44492400, 0x7a8f4683, 0xf04f4692, 0x2d3c0801, 0xd82e4620, 0x60b04e1a, 0xf3c07ac8, 0xf3c001c1,
    0xf7ff1041, 0x6830ffd4, 0x7040f440, 0xb2a86030, 0x20036070, 0x0118f8c6, 0xf08bfa9b, 0x0100ea47,
    0xf7ff2002, 0x2001ff92, 0xf7fe60b0, 0xb958fbec, 0xe00b46a0, 0x07006ab0, 0x2000d506, 0xff92f7ff,
    0x0004f80a, 0xb2e41c64, 0xd3f342ac, 0x60b02000, 0xe8bd4640, 0x00008df0, 0x10000100, 0x40007000,
    0x40080000, 0x0000003c, 0x4080f04f, 0x1230f8d0, 0x0140f041, 0x1230f8c0, 0x1360f8d0, 0x7180f441,
    0x1360f8c0, 0x1210f8d0, 0x3180f441, 0x1210f8c0, 0xb5104770, 0x2001b900, 0x68234c15, 0x030ff360,
    0x635cf361, 0x735ef362, 0xbd106023, 0x68084910, 0xf36222a5, 0xf0404017, 0x60084001, 0x490c4770,
    0x22006808, 0x4017f362, 0x4001f040, 0x47706008, 0x68014807, 0x7180f041, 0x47706001, 0xf7ff4602,
    0x2100ffc3, 0xf7ff2001, 0xf7ffffd4, 0xe7feffdf, 0x40006000, 0x68414808, 0x0101f041, 0x68416041,
    0xd5fc0789, 0x60412100, 0x4a034770, 0x430168d1, 0x438160d1, 0x477060d1, 0x40007000, 0x47704770,
    0x00004770, 0x68c2b510, 0x0280f022, 0x220060c2, 0x69426042, 0xf0426882, 0x60820206, 0xf04268c2,
    0x60c20280, 0xf0226a02, 0x620202f0, 0x888b6a02, 0x1203ea42, 0x69c26202, 0x401a4b64, 0x69c261c2,
    0xea42880b, 0x61c24203, 0x6002788a, 0x0a12884a, 0x68c26042, 0x0280f022, 0x890a60c2, 0x431a894b,
    0x431a88cb, 0x89ca60c2, 0xeb032301, 0x8a0b2202, 0x6082431a, 0xf0226902, 0x61020222, 0x898b6902,
    0x6102431a, 0x64028a4a, 0x2a088a0a, 0x8acad11a, 0x6a82b152, 0x02f8f022, 0x6a826282, 0x24027d0b,
    0x03c3ea44, 0x6282431a, 0x2a008b0a, 0x6a82d00a, 0x527cf422, 0x6a826282, 0x23047d49, 0x2101ea43,
    0x6282430a, 0x4942bd10, 0xd1034288, 0x49412200, 0xe00e4841, 0x42884941, 0x2200d104, 0x2110f04f,
    0xe0061480, 0x4288493e, 0x483bd105, 0x493d2200, 0xf0001c40, 0x4770b879, 0x80412114, 0x8081210c,
    0x2152f240, 0x21008001, 0x81418101, 0x80c22201, 0x81818201, 0x81c32310, 0x230f8242, 0x75427503,
    0x830182c1, 0xe0024770, 0xf8016a43, 0x1e523b01, 0xd2f9b292, 0xe0024770, 0x3b01f811, 0x1e526243,
    0xd2f9b292, 0x060b4770, 0x2a01d50d, 0x6c03d013, 0x4300f023, 0x6c436403, 0x0301f043, 0x6c836443,
    0x0301f023, 0x070b6483, 0x2a01d004, 0xd0136842, 0x6042438a, 0x6a034770, 0x0308f043, 0x6a036203,
    0x0308f023, 0x6c836203, 0x0301f043, 0x6c036483, 0x4300f043, 0xe7e66403, 0xe7ea430a, 0x20004602,
    0x7f80f5b1, 0x6952d004, 0xd000420a, 0x47702001, 0x07c96c51, 0x4770d1fa, 0x69012901, 0xf021d003,
    0x61010110, 0xf0414770, 0xe7fa0110, 0xf800ffff, 0x40012000, 0x20000001, 0x08000001, 0x40011000,
    0x40024000, 0x10000400, 0xf3c0b570, 0xf3c16581, 0x2a017301, 0x0794d135, 0x5f44f1b1, 0xf1a1d017,
    0x3e405640, 0xf1a1d013, 0x3e105640, 0x4eb7d002, 0xd11742b1, 0x620cf8d4, 0x6680f046, 0x620cf8c4,
    0x620cf8d4, 0x6600f046, 0x620cf8c4, 0xf8d4e019, 0xf046620c, 0xf8c46680, 0xf8d4620c, 0xf046620c,
    0xe7f15600, 0x42b14eaa, 0xf8d4d10b, 0xf4466360, 0xf8c47600, 0xf8d46360, 0xf0466348, 0xf8c40610,
    0xf0206348, 0xf0216440, 0xea4f5040, 0xf1010185, 0x2a014180, 0x2210f8d1, 0x43a2d00d, 0x2210f8c1,
    0xf1010099, 0xf8d14180, 0x4382222c, 0x0040ea22, 0x022cf8c1, 0x4322bd70, 0x2210f8c1, 0xf1010099,
    0xf8d14180, 0x4302222c, 0x0040ea42, 0xf04fe7f0, 0x29014280, 0x120cf8d2, 0x4381d003, 0x120cf8c2,
    0xf4414770, 0xf8c21180, 0xf8d2120c, 0xf441120c, 0xf8c21100, 0xf8d2120c, 0xf441120c, 0xf8c20180,
    0xf8d2120c, 0xf041120c, 0xf8c26180, 0xf8d2120c, 0x4301120c, 0xb570e7e2, 0x497e460d, 0x4480f04f,
    0xd11d4288, 0x0234f8d4, 0x3080f420, 0x0234f8c4, 0xf5042001, 0xf7fe740d, 0xf8d4f843, 0xf4200128,
    0xf8c410c0, 0xf8d40128, 0xea400128, 0xf8c440c5, 0x20010128, 0xf834f7fe, 0xf4406820, 0xe01f3080,
    0x4288496d, 0xf8d4d11d, 0xf4200234, 0xf8c42080, 0x20010234, 0x740df504, 0xf822f7fe, 0x0128f8d4,
    0x00c0f420, 0x0128f8c4, 0x0128f8d4, 0x5045ea40, 0x0128f8c4, 0xf7fe2001, 0x6820f813, 0x2080f440,
    0xbd706020, 0x460db570, 0x048c495c, 0xd11d4288, 0x0238f8d4, 0x0001f020, 0x0238f8c4, 0xf5042001,
    0xf7fd740e, 0xf8d4fffd, 0xf4200124, 0xf8c430c0, 0xf8d40124, 0xea400124, 0xf8c430c5, 0x20010124,
    0xffeef7fd, 0xf0406820, 0xe01f0001, 0x4288494c, 0xf8d4d11d, 0xf0200238, 0xf8c40004, 0x20010238,
    0x740ef504, 0xffdcf7fd, 0x0124f8d4, 0x20c0f420, 0x0124f8c4, 0x0124f8d4, 0x4045ea40, 0x0124f8c4,
    0xf7fd2001, 0x6820ffcd, 0x0004f040, 0xbd706020, 0x460db570, 0x044c493b, 0xd11d4288, 0x0234f8d4,
    0x0001f020, 0x0234f8c4, 0xf5042001, 0xf7fd740d, 0xf8d4ffb7, 0xf4200128, 0xf8c460c0, 0xf8d40128,
    0xea400128, 0xf8c42045, 0x20010128, 0xffa8f7fd, 0xf0406820, 0xe01f0001, 0x4288492b, 0xf8d4d11d,
    0xf4200230, 0xf8c45080, 0x20010230, 0x740cf504, 0xff96f7fd, 0x012cf8d4, 0x50c0f420, 0x012cf8c4,
    0x012cf8d4, 0x20c5ea40, 0x012cf8c4, 0xf7fd2001, 0x6820ff87, 0x5080f440, 0xbd706020, 0x7201f3c0,
    0xea4f2901, 0xf1010182, 0xf0204180, 0xf8d15040, 0xd005222c, 0xea224382, 0xf8c10040, 0x4770022c,
    0xea424302, 0xe7f80040, 0x6281f3c0, 0xea4f2901, 0xf1010182, 0xf0204180, 0xf8d16040, 0xd0032210,
    0xf8c14382, 0x47702210, 0xe7fa4302, 0x30010000, 0x10004000, 0x40013000, 0x40013400, 0x40015000,
    0x40015400, 0x40012000, 0x40011000, 0x07800882, 0x00920ec0, 0xf102b510, 0xf8d24280, 0x24ff3280,
    0x43a34084, 0x430b4081, 0x3280f8c2, 0x0881bd10, 0xf1010089, 0xf8d14180, 0x07802280, 0x20ff0ec3,
    0x43824098, 0x2280f8c1, 0x20004770, 0x00824601, 0x4280f102, 0x1280f8c2, 0xb2c01c40, 0xd3f6280a,
    0xe92d4770, 0x460f47f0, 0xa808e9dd, 0x461d49a7, 0x44794616, 0x4010f811, 0xf0004620, 0xf020f97e,
    0x2d01000f, 0x2d02d002, 0xe004d003, 0x0004f040, 0xf040e001, 0xea48000c, 0x4301014a, 0x4620b2c9,
    0xf955f000, 0xf0001c60, 0xb116f968, 0x0001f040, 0xf020e001, 0xb1170001, 0x0102f040, 0xf020e001,
    0x1c600102, 0x47f0e8bd, 0xb941f000, 0x4604b510, 0xf000202b, 0xf020f952, 0xf004013f, 0x4308003f,
    0x01c0f040, 0x4010e8bd, 0xf000202b, 0xb570b930, 0x4986460d, 0x39824479, 0x4010f811, 0xf0001c60,
    0xb115f93c, 0x0104f040, 0xf020e001, 0x1c600104, 0x4070e8bd, 0xb91bf000, 0x460db570, 0x4479497b,
    0xf81139ac, 0x46204010, 0xf927f000, 0xf040b115, 0xe0010120, 0x0120f020, 0xe8bd4620, 0xf0004070,
    0xb570b906, 0x4971460d, 0x39d64479, 0x4010f811, 0xf0004620, 0xb115f912, 0x0140f040, 0xf020e001,
    0x46200140, 0x4070e8bd, 0xb8f1f000, 0x4615b570, 0xf7ff4604, 0x2101ffe6, 0xf7ff4620, 0x4629ffcd,
    0xe8bd4620, 0xe7b24070, 0xe7c52100, 0x495fb570, 0x44792400, 0xf83139d2, 0xf4200010, 0x0b024170,
    0x40902001, 0x4608b2c5, 0xf8e7f000, 0xd0004228, 0x46202401, 0xe7e9bd70, 0x21ffb510, 0xf000209a,
    0x21fff8c6, 0xf000209b, 0x21fff8c2, 0xf00020ae, 0x21fff8be, 0xf00020d2, 0x21fff8ba, 0xf00020f4,
    0x20f5f8b6, 0xf8c9f000, 0x0103f040, 0x4010e8bd, 0xf00020f5, 0xb570b8ac, 0x4945460d, 0xf8114479,
    0x46204010, 0xf8b9f000, 0xf040b115, 0xe0010102, 0x0102f020, 0xe8bd4620, 0xf0004070, 0xb570b898,
    0x493b460d, 0x39284479, 0x4010f811, 0xf0004620, 0xb115f8a4, 0x0101f040, 0xf020e001, 0x46200101,
    0x4070e8bd, 0xb883f000, 0x460db570, 0x44794930, 0xf8113952, 0x46204010, 0xf88ff000, 0xf040b115,
    0xe0010104, 0x0104f020, 0xe8bd4620, 0xf0004070, 0xb570b86e, 0x4926460d, 0x397c4479, 0x4010f811,
    0xf0004620, 0xb115f87a, 0x0108f040, 0xf020e001, 0x46200108, 0x4070e8bd, 0xb859f000, 0x460db570,
    0x4479491b, 0xf81139a6, 0x1c604010, 0xf865f000, 0xf040b115, 0xe0010102, 0x0102f020, 0xe8bd1c60,
    0xf0004070, 0x4912b844, 0x397e4479, 0x1010f831, 0x4070f421, 0x21010b0a, 0xb2c94091, 0xb837f000,
    0x460db570, 0x4479490a, 0xf81139ea, 0x46204010, 0xf843f000, 0xf040b115, 0xe0010101, 0x0101f020,
    0xe8bd4620, 0xf0004070, 0x0000b822, 0x0000060a, 0x00000480, 0xf3602100, 0xf04f4159, 0xf0214080,
    0x64810101, 0xf3c06c80, 0x47702047, 0xf3602200, 0xf3614259, 0xf04f0248, 0xf0224180, 0x64880001,
    0x0001f040, 0xf0206488, 0x64880001, 0xb5104770, 0x4280f04f, 0xf0236c93, 0x23000401, 0x4359f360,
    0x0348f361, 0x0001f023, 0xf0406490, 0x64900001, 0x0001f020, 0x64946490, 0xf04fbd10, 0x6c8a4180,
    0xf3602300, 0xf0234359, 0xf0220001, 0x64880201, 0x648a6c88, 0x2047f3c0, 0xea404770, 0xb5100301,
    0xd10f079b, 0xd30d2a04, 0xc908c810, 0x429c1f12, 0xba20d0f8, 0x4288ba19, 0x2001d901, 0xf04fbd10,
    0xbd1030ff, 0x07d3b11a, 0x1c52d003, 0x2000e007, 0xf810bd10, 0xf8113b01, 0x1b1b4b01, 0xf810d107,
    0xf8113b01, 0x1b1b4b01, 0x1e92d101, 0x4618d1f1, 0x0000bd10, 0x2012c205, 0x00040000, 0x00000303,
    0x2016c20b, 0x00400000, 0x00000707, 0x2017c20b, 0x00800000, 0x00000f08, 0x2314c20b, 0x00100000,
    0x00000f05, 0x2811c20b, 0x00020000, 0x00000302, 0x2812c20b, 0x00040000, 0x00000303, 0x2814c20b,
    0x00100000, 0x00000f05, 0x2816c20b, 0x00400000, 0x00000f07, 0x2817c20b, 0x00800000, 0x00000f08,
    0x4014ef05, 0x00100000, 0x00000705, 0x4015ef05, 0x00200000, 0x00000706, 0x4016ef05, 0x00400000,
    0x00000707, 0x4017ef05, 0x00800000, 0x00000707, 0x6012ef05, 0x00040000, 0x00000303, 0x6014ef05,
    0x00100000, 0x00000705, 0x4013c805, 0x00080000, 0x00000704, 0x4014c805, 0x00100000, 0x00000705,
    0x4015c805, 0x00200000, 0x00000706, 0x4016c805, 0x00400000, 0x00000707, 0x4017c805, 0x00800000,
    0x00000707, 0x4018c805, 0x01000000, 0x00000707, 0x6015c805, 0x00200000, 0x00000706, 0x6016c805,
    0x00400000, 0x00000707, 0x6412c87f, 0x00040000, 0x00000706, 0x6413c87f, 0x00080000, 0x00000707,
    0x6414c8ff, 0x00100000, 0x00000707, 0x30141c05, 0x00100000, 0x00000705, 0x38151c05, 0x00200000,
    0x00000706, 0x70151c05, 0x00200000, 0x00000706, 0x70161c05, 0x00400000, 0x00000707, 0x2812a1ff,
    0x00040000, 0x00000703, 0x2813a105, 0x00080000, 0x00000704, 0x4013a105, 0x00080000, 0x00000704,
    0x4014a105, 0x00100000, 0x00000705, 0x4015a105, 0x00200000, 0x00000706, 0x60138505, 0x00080000,
    0x00000705, 0x60188505, 0x01000000, 0x00000707, 0x40130b0e, 0x00080000, 0x00000704, 0x40140b05,
    0x00100000, 0x00000f05, 0x40150b05, 0x00200000, 0x00000706, 0x40160b05, 0x00400000, 0x00000707,
    0x40170b05, 0x00800000, 0x00000707, 0x40180b05, 0x01000000, 0x00000707, 0x60120b7f, 0x00040000,
    0x00000303, 0x60160b05, 0x00400000, 0x00000707, 0x60182009, 0x01000000, 0x00000f09, 0x60172009,
    0x00800000, 0x00000f08, 0x32145eff, 0x00100000, 0x00000707, 0x40185e05, 0x01000000, 0x00000707,
    0x21185205, 0x01000000, 0x00000707, 0x40176805, 0x00800000, 0x00000707, 0x00000000, 0x00010000,
    0x00020000, 0x00040000, 0x00080000, 0x00100000, 0x00200000, 0x00400000, 0x00800000, 0x00000028,
    0x00e200e0, 0x00e600e4, 0x00a000e8, 0x00a400a2, 0x00ec00ea, 0x00f000ee, 0x008000f2, 0x00840082,
    0x00c200c0, 0x00c600c4, 0x00ca00c8, 0x00ce00cc, 0x00880086, 0x008c008a, 0x0090008e, 0x00000092,
    0x00a800a6, 0x00ac00aa, 0x009600d0, 0x00f40098, 0x20f410f4, 0x40f430f4, 0x10ae00ae, 0x50f420ae,
    0x70f460f4, 0x10f500f5, 0x109a009a, 0x00d2209a, 0x20d210d2, 0x40d230d2, 0x60d250d2, 0x309a70d2,
    0x509a409a, 0x709a609a, 0x00f4009b, 0x30ae0000, 0x50ae40ae, 0x00d360ae, 0x409b309b, 0x3a66666f,
    0x2c642520, 0x6e616d20, 0x64695f75, 0x3025203a, 0x202c5832, 0x5f766564, 0x203a6469, 0x58343025,
    0x6973202c, 0x203a657a, 0x202c6425, 0x615f7062, 0x6c5f6c6c, 0x25203a76, 0x62202c64, 0x616d5f70,
    0x203a6b73, 0x58323025, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000020, 0x00000000,
    0x02625a00, 0x00080000, 0x0009000c, 0xab000600, 0x29000000, 0x27100000, 0x00990066, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x002000a1,
    'pc_unInit': 0x0020011f,
    'pc_program_page': 0x002001c9,
    'pc_erase_sector': 0x00200187,
    'pc_eraseAll': 0x00200173,

    'static_base' : 0x00200000 + 0x00000004 + 0x000028cc,
    'begin_stack' : 0x00205960,
    'end_stack' : 0x00204960,
    'begin_data' : 0x00200000 + 0x1000,
    'page_size' : 0x1000,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x00202960,
        0x00203960
    ],
    'min_program_length' : 0x1000,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0x28cc,
    'rw_start': 0x28d0,
    'rw_size': 0x3c,
    'zi_start': 0x290c,
    'zi_size': 0x50,

    # Flash information
    'flash_start': 0x800000,
    'flash_size': 0x1000000,
    'sector_sizes': (
        (0x0, 0x1000),
    )
}

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)

class RTL8762C(CoreSightTarget):

    VENDOR = "Realtek Semiconductor"

    MEMORY_MAP = MemoryMap(
        FlashRegion(    start=0x800000,  length=0x1000000, blocksize=0x800, is_boot_memory=True, algo=FLASH_ALGO),
        RamRegion(      start=0x200000,  length=0x24000),
        RamRegion(      start=0x224000,  length=0x2000),
        RamRegion(      start=0x226000,  length=0x2000),
        RamRegion(      start=0x280000,  length=0x8000)
        )

    def __init__(self, session):
        super(RTL8762C, self).__init__(session, self.MEMORY_MAP)