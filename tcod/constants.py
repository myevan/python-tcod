"""
    Constants from the libtcod C API.

    This module is auto-generated by `build_libtcod.py`.
"""
from __future__ import absolute_import

from tcod.color import Color

FOV_BASIC = 0
FOV_DIAMOND = 1
FOV_PERMISSIVE_0 = 3
FOV_PERMISSIVE_1 = 4
FOV_PERMISSIVE_2 = 5
FOV_PERMISSIVE_3 = 6
FOV_PERMISSIVE_4 = 7
FOV_PERMISSIVE_5 = 8
FOV_PERMISSIVE_6 = 9
FOV_PERMISSIVE_7 = 10
FOV_PERMISSIVE_8 = 11
FOV_RESTRICTIVE = 12
FOV_SHADOW = 2
KEY_0 = 24
KEY_1 = 25
KEY_2 = 26
KEY_3 = 27
KEY_4 = 28
KEY_5 = 29
KEY_6 = 30
KEY_7 = 31
KEY_8 = 32
KEY_9 = 33
KEY_ALT = 7
KEY_APPS = 23
KEY_BACKSPACE = 2
KEY_CAPSLOCK = 9
KEY_CHAR = 65
KEY_CONTROL = 6
KEY_DELETE = 20
KEY_DOWN = 17
KEY_END = 12
KEY_ENTER = 4
KEY_ESCAPE = 1
KEY_F1 = 50
KEY_F10 = 59
KEY_F11 = 60
KEY_F12 = 61
KEY_F2 = 51
KEY_F3 = 52
KEY_F4 = 53
KEY_F5 = 54
KEY_F6 = 55
KEY_F7 = 56
KEY_F8 = 57
KEY_F9 = 58
KEY_HOME = 13
KEY_INSERT = 19
KEY_KP0 = 34
KEY_KP1 = 35
KEY_KP2 = 36
KEY_KP3 = 37
KEY_KP4 = 38
KEY_KP5 = 39
KEY_KP6 = 40
KEY_KP7 = 41
KEY_KP8 = 42
KEY_KP9 = 43
KEY_KPADD = 44
KEY_KPDEC = 48
KEY_KPDIV = 46
KEY_KPENTER = 49
KEY_KPMUL = 47
KEY_KPSUB = 45
KEY_LEFT = 15
KEY_LWIN = 21
KEY_NONE = 0
KEY_NUMLOCK = 62
KEY_PAGEDOWN = 11
KEY_PAGEUP = 10
KEY_PAUSE = 8
KEY_PRINTSCREEN = 18
KEY_RIGHT = 16
KEY_RWIN = 22
KEY_SCROLLLOCK = 63
KEY_SHIFT = 5
KEY_SPACE = 64
KEY_TAB = 3
KEY_TEXT = 66
KEY_UP = 14
BKGND_ADD = 8
BKGND_ADDA = 9
BKGND_ALPH = 12
BKGND_BURN = 10
BKGND_COLOR_BURN = 7
BKGND_COLOR_DODGE = 6
BKGND_DARKEN = 4
BKGND_DEFAULT = 13
BKGND_LIGHTEN = 3
BKGND_MULTIPLY = 2
BKGND_NONE = 0
BKGND_OVERLAY = 11
BKGND_SCREEN = 5
BKGND_SET = 1
CENTER = 2
CHAR_ARROW2_E = 16
CHAR_ARROW2_N = 30
CHAR_ARROW2_S = 31
CHAR_ARROW2_W = 17
CHAR_ARROW_E = 26
CHAR_ARROW_N = 24
CHAR_ARROW_S = 25
CHAR_ARROW_W = 27
CHAR_BLOCK1 = 176
CHAR_BLOCK2 = 177
CHAR_BLOCK3 = 178
CHAR_BULLET = 7
CHAR_BULLET_INV = 8
CHAR_BULLET_SQUARE = 254
CHAR_CENT = 189
CHAR_CHECKBOX_SET = 225
CHAR_CHECKBOX_UNSET = 224
CHAR_CLUB = 5
CHAR_COPYRIGHT = 184
CHAR_CROSS = 197
CHAR_CURRENCY = 207
CHAR_DARROW_H = 29
CHAR_DARROW_V = 18
CHAR_DCROSS = 206
CHAR_DHLINE = 205
CHAR_DIAMOND = 4
CHAR_DIVISION = 246
CHAR_DNE = 187
CHAR_DNW = 201
CHAR_DSE = 188
CHAR_DSW = 200
CHAR_DTEEE = 204
CHAR_DTEEN = 202
CHAR_DTEES = 203
CHAR_DTEEW = 185
CHAR_DVLINE = 186
CHAR_EXCLAM_DOUBLE = 19
CHAR_FEMALE = 12
CHAR_FUNCTION = 159
CHAR_GRADE = 248
CHAR_HALF = 171
CHAR_HEART = 3
CHAR_HLINE = 196
CHAR_LIGHT = 15
CHAR_MALE = 11
CHAR_MULTIPLICATION = 158
CHAR_NE = 191
CHAR_NOTE = 13
CHAR_NOTE_DOUBLE = 14
CHAR_NW = 218
CHAR_ONE_QUARTER = 172
CHAR_PILCROW = 20
CHAR_POUND = 156
CHAR_POW1 = 251
CHAR_POW2 = 253
CHAR_POW3 = 252
CHAR_RADIO_SET = 10
CHAR_RADIO_UNSET = 9
CHAR_RESERVED = 169
CHAR_SE = 217
CHAR_SECTION = 21
CHAR_SMILIE = 1
CHAR_SMILIE_INV = 2
CHAR_SPADE = 6
CHAR_SUBP_DIAG = 230
CHAR_SUBP_E = 231
CHAR_SUBP_N = 228
CHAR_SUBP_NE = 227
CHAR_SUBP_NW = 226
CHAR_SUBP_SE = 229
CHAR_SUBP_SW = 232
CHAR_SW = 192
CHAR_TEEE = 195
CHAR_TEEN = 193
CHAR_TEES = 194
CHAR_TEEW = 180
CHAR_THREE_QUARTERS = 243
CHAR_UMLAUT = 249
CHAR_VLINE = 179
CHAR_YEN = 190
COLCTRL_1 = 1
COLCTRL_2 = 2
COLCTRL_3 = 3
COLCTRL_4 = 4
COLCTRL_5 = 5
COLCTRL_BACK_RGB = 7
COLCTRL_FORE_RGB = 6
COLCTRL_NUMBER = 5
COLCTRL_STOP = 8
COLOR_AMBER = 3
COLOR_AZURE = 12
COLOR_BLUE = 13
COLOR_CHARTREUSE = 6
COLOR_CRIMSON = 20
COLOR_CYAN = 10
COLOR_DARK = 5
COLOR_DARKER = 6
COLOR_DARKEST = 7
COLOR_DESATURATED = 0
COLOR_FLAME = 1
COLOR_FUCHSIA = 17
COLOR_GREEN = 7
COLOR_HAN = 14
COLOR_LEVELS = 8
COLOR_LIGHT = 3
COLOR_LIGHTER = 2
COLOR_LIGHTEST = 1
COLOR_LIME = 5
COLOR_MAGENTA = 18
COLOR_NB = 21
COLOR_NORMAL = 4
COLOR_ORANGE = 2
COLOR_PINK = 19
COLOR_PURPLE = 16
COLOR_RED = 0
COLOR_SEA = 8
COLOR_SKY = 11
COLOR_TURQUOISE = 9
COLOR_VIOLET = 15
COLOR_YELLOW = 4
DISTRIBUTION_GAUSSIAN = 1
DISTRIBUTION_GAUSSIAN_INVERSE = 3
DISTRIBUTION_GAUSSIAN_RANGE = 2
DISTRIBUTION_GAUSSIAN_RANGE_INVERSE = 4
DISTRIBUTION_LINEAR = 0
EVENT_ANY = 255
EVENT_FINGER = 224
EVENT_FINGER_MOVE = 32
EVENT_FINGER_PRESS = 64
EVENT_FINGER_RELEASE = 128
EVENT_KEY = 3
EVENT_KEY_PRESS = 1
EVENT_KEY_RELEASE = 2
EVENT_MOUSE = 28
EVENT_MOUSE_MOVE = 4
EVENT_MOUSE_PRESS = 8
EVENT_MOUSE_RELEASE = 16
EVENT_NONE = 0
FONT_LAYOUT_ASCII_INCOL = 1
FONT_LAYOUT_ASCII_INROW = 2
FONT_LAYOUT_CP437 = 16
FONT_LAYOUT_TCOD = 8
FONT_TYPE_GRAYSCALE = 4
FONT_TYPE_GREYSCALE = 4
KEY_PRESSED = 1
KEY_RELEASED = 2
LEFT = 0
NB_RENDERERS = 5
NOISE_DEFAULT = 0
NOISE_PERLIN = 1
NOISE_SIMPLEX = 2
NOISE_WAVELET = 4
RENDERER_GLSL = 0
RENDERER_OPENGL = 1
RENDERER_OPENGL2 = 4
RENDERER_SDL = 2
RENDERER_SDL2 = 3
RIGHT = 1
RNG_CMWC = 1
RNG_MT = 0
TYPE_BOOL = 1
TYPE_CHAR = 2
TYPE_COLOR = 6
TYPE_CUSTOM00 = 24
TYPE_CUSTOM01 = 25
TYPE_CUSTOM02 = 26
TYPE_CUSTOM03 = 27
TYPE_CUSTOM04 = 28
TYPE_CUSTOM05 = 29
TYPE_CUSTOM06 = 30
TYPE_CUSTOM07 = 31
TYPE_CUSTOM08 = 32
TYPE_CUSTOM09 = 33
TYPE_CUSTOM10 = 34
TYPE_CUSTOM11 = 35
TYPE_CUSTOM12 = 36
TYPE_CUSTOM13 = 37
TYPE_CUSTOM14 = 38
TYPE_CUSTOM15 = 39
TYPE_DICE = 7
TYPE_FLOAT = 4
TYPE_INT = 3
TYPE_LIST = 1024
TYPE_NONE = 0
TYPE_STRING = 5
TYPE_VALUELIST00 = 8
TYPE_VALUELIST01 = 9
TYPE_VALUELIST02 = 10
TYPE_VALUELIST03 = 11
TYPE_VALUELIST04 = 12
TYPE_VALUELIST05 = 13
TYPE_VALUELIST06 = 14
TYPE_VALUELIST07 = 15
TYPE_VALUELIST08 = 16
TYPE_VALUELIST09 = 17
TYPE_VALUELIST10 = 18
TYPE_VALUELIST11 = 19
TYPE_VALUELIST12 = 20
TYPE_VALUELIST13 = 21
TYPE_VALUELIST14 = 22
TYPE_VALUELIST15 = 23

# --- colors ---
amber = Color(255,191,0)
azure = Color(0,127,255)
black = Color(0,0,0)
blue = Color(0,0,255)
brass = Color(191,151,96)
celadon = Color(172,255,175)
chartreuse = Color(127,255,0)
copper = Color(197,136,124)
crimson = Color(255,0,63)
cyan = Color(0,255,255)
dark_amber = Color(191,143,0)
dark_azure = Color(0,95,191)
dark_blue = Color(0,0,191)
dark_chartreuse = Color(95,191,0)
dark_crimson = Color(191,0,47)
dark_cyan = Color(0,191,191)
dark_flame = Color(191,47,0)
dark_fuchsia = Color(191,0,191)
dark_gray = Color(95,95,95)
dark_green = Color(0,191,0)
dark_grey = Color(95,95,95)
dark_han = Color(47,0,191)
dark_lime = Color(143,191,0)
dark_magenta = Color(191,0,143)
dark_orange = Color(191,95,0)
dark_pink = Color(191,0,95)
dark_purple = Color(143,0,191)
dark_red = Color(191,0,0)
dark_sea = Color(0,191,95)
dark_sepia = Color(94,75,47)
dark_sky = Color(0,143,191)
dark_turquoise = Color(0,191,143)
dark_violet = Color(95,0,191)
dark_yellow = Color(191,191,0)
darker_amber = Color(127,95,0)
darker_azure = Color(0,63,127)
darker_blue = Color(0,0,127)
darker_chartreuse = Color(63,127,0)
darker_crimson = Color(127,0,31)
darker_cyan = Color(0,127,127)
darker_flame = Color(127,31,0)
darker_fuchsia = Color(127,0,127)
darker_gray = Color(63,63,63)
darker_green = Color(0,127,0)
darker_grey = Color(63,63,63)
darker_han = Color(31,0,127)
darker_lime = Color(95,127,0)
darker_magenta = Color(127,0,95)
darker_orange = Color(127,63,0)
darker_pink = Color(127,0,63)
darker_purple = Color(95,0,127)
darker_red = Color(127,0,0)
darker_sea = Color(0,127,63)
darker_sepia = Color(63,50,31)
darker_sky = Color(0,95,127)
darker_turquoise = Color(0,127,95)
darker_violet = Color(63,0,127)
darker_yellow = Color(127,127,0)
darkest_amber = Color(63,47,0)
darkest_azure = Color(0,31,63)
darkest_blue = Color(0,0,63)
darkest_chartreuse = Color(31,63,0)
darkest_crimson = Color(63,0,15)
darkest_cyan = Color(0,63,63)
darkest_flame = Color(63,15,0)
darkest_fuchsia = Color(63,0,63)
darkest_gray = Color(31,31,31)
darkest_green = Color(0,63,0)
darkest_grey = Color(31,31,31)
darkest_han = Color(15,0,63)
darkest_lime = Color(47,63,0)
darkest_magenta = Color(63,0,47)
darkest_orange = Color(63,31,0)
darkest_pink = Color(63,0,31)
darkest_purple = Color(47,0,63)
darkest_red = Color(63,0,0)
darkest_sea = Color(0,63,31)
darkest_sepia = Color(31,24,15)
darkest_sky = Color(0,47,63)
darkest_turquoise = Color(0,63,47)
darkest_violet = Color(31,0,63)
darkest_yellow = Color(63,63,0)
desaturated_amber = Color(127,111,63)
desaturated_azure = Color(63,95,127)
desaturated_blue = Color(63,63,127)
desaturated_chartreuse = Color(95,127,63)
desaturated_crimson = Color(127,63,79)
desaturated_cyan = Color(63,127,127)
desaturated_flame = Color(127,79,63)
desaturated_fuchsia = Color(127,63,127)
desaturated_green = Color(63,127,63)
desaturated_han = Color(79,63,127)
desaturated_lime = Color(111,127,63)
desaturated_magenta = Color(127,63,111)
desaturated_orange = Color(127,95,63)
desaturated_pink = Color(127,63,95)
desaturated_purple = Color(111,63,127)
desaturated_red = Color(127,63,63)
desaturated_sea = Color(63,127,95)
desaturated_sky = Color(63,111,127)
desaturated_turquoise = Color(63,127,111)
desaturated_violet = Color(95,63,127)
desaturated_yellow = Color(127,127,63)
flame = Color(255,63,0)
fuchsia = Color(255,0,255)
gold = Color(229,191,0)
gray = Color(127,127,127)
green = Color(0,255,0)
grey = Color(127,127,127)
han = Color(63,0,255)
light_amber = Color(255,207,63)
light_azure = Color(63,159,255)
light_blue = Color(63,63,255)
light_chartreuse = Color(159,255,63)
light_crimson = Color(255,63,111)
light_cyan = Color(63,255,255)
light_flame = Color(255,111,63)
light_fuchsia = Color(255,63,255)
light_gray = Color(159,159,159)
light_green = Color(63,255,63)
light_grey = Color(159,159,159)
light_han = Color(111,63,255)
light_lime = Color(207,255,63)
light_magenta = Color(255,63,207)
light_orange = Color(255,159,63)
light_pink = Color(255,63,159)
light_purple = Color(207,63,255)
light_red = Color(255,63,63)
light_sea = Color(63,255,159)
light_sepia = Color(158,134,100)
light_sky = Color(63,207,255)
light_turquoise = Color(63,255,207)
light_violet = Color(159,63,255)
light_yellow = Color(255,255,63)
lighter_amber = Color(255,223,127)
lighter_azure = Color(127,191,255)
lighter_blue = Color(127,127,255)
lighter_chartreuse = Color(191,255,127)
lighter_crimson = Color(255,127,159)
lighter_cyan = Color(127,255,255)
lighter_flame = Color(255,159,127)
lighter_fuchsia = Color(255,127,255)
lighter_gray = Color(191,191,191)
lighter_green = Color(127,255,127)
lighter_grey = Color(191,191,191)
lighter_han = Color(159,127,255)
lighter_lime = Color(223,255,127)
lighter_magenta = Color(255,127,223)
lighter_orange = Color(255,191,127)
lighter_pink = Color(255,127,191)
lighter_purple = Color(223,127,255)
lighter_red = Color(255,127,127)
lighter_sea = Color(127,255,191)
lighter_sepia = Color(191,171,143)
lighter_sky = Color(127,223,255)
lighter_turquoise = Color(127,255,223)
lighter_violet = Color(191,127,255)
lighter_yellow = Color(255,255,127)
lightest_amber = Color(255,239,191)
lightest_azure = Color(191,223,255)
lightest_blue = Color(191,191,255)
lightest_chartreuse = Color(223,255,191)
lightest_crimson = Color(255,191,207)
lightest_cyan = Color(191,255,255)
lightest_flame = Color(255,207,191)
lightest_fuchsia = Color(255,191,255)
lightest_gray = Color(223,223,223)
lightest_green = Color(191,255,191)
lightest_grey = Color(223,223,223)
lightest_han = Color(207,191,255)
lightest_lime = Color(239,255,191)
lightest_magenta = Color(255,191,239)
lightest_orange = Color(255,223,191)
lightest_pink = Color(255,191,223)
lightest_purple = Color(239,191,255)
lightest_red = Color(255,191,191)
lightest_sea = Color(191,255,223)
lightest_sepia = Color(222,211,195)
lightest_sky = Color(191,239,255)
lightest_turquoise = Color(191,255,239)
lightest_violet = Color(223,191,255)
lightest_yellow = Color(255,255,191)
lime = Color(191,255,0)
magenta = Color(255,0,191)
orange = Color(255,127,0)
peach = Color(255,159,127)
pink = Color(255,0,127)
purple = Color(191,0,255)
red = Color(255,0,0)
sea = Color(0,255,127)
sepia = Color(127,101,63)
silver = Color(203,203,203)
sky = Color(0,191,255)
turquoise = Color(0,255,191)
violet = Color(127,0,255)
white = Color(255,255,255)
yellow = Color(255,255,0)
