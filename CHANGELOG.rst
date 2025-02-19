===========
 Changelog
===========
Changes relevant to the users of python-tcod are documented here.

This project adheres to `Semantic Versioning <https://semver.org/>`_ since
v2.0.0

Unreleased
------------------

11.1.0 - 2019-07-05
-------------------
Added
 - You can now set the `TCOD_RENDERER` and `TCOD_VSYNC` environment variables to
   force specific options to be used.
   Example: ``TCOD_RENDERER=sdl2 TCOD_VSYNC=1``

Changed
 - `tcod.sys_set_renderer` now raises an exception if it fails.

Fixed
 - `tcod.console_map_ascii_code_to_font` functions will now work when called
   before `tcod.console_init_root`.

11.0.2 - 2019-06-21
-------------------
Changed
 - You no longer need OpenGL to build python-tcod.

11.0.1 - 2019-06-21
-------------------
Changed
 - Better runtime checks for Windows dependencies should now give distinct
   errors depending on if the issue is SDL2 or missing redistributables.

Fixed
 - Changed NumPy type hints from `np.array` to `np.ndarray` which should
   resolve issues.

11.0.0 - 2019-06-14
-------------------
Changed
 - `tcod.map.compute_fov` now takes a 2-item tuple instead of separate `x` and
   `y` parameters.  This causes less confusion over how axes are aligned.

10.1.1 - 2019-06-02
-------------------
Changed
 - Better string representations for `tcod.event.Event` subclasses.

Fixed
 - Fixed regressions in text alignment for non-rectangle print functions.

10.1.0 - 2019-05-24
-------------------
Added
 - `tcod.console_init_root` now has an optional `vsync` parameter.

10.0.5 - 2019-05-17
-------------------
Fixed
 - Fixed shader compilation issues in the OPENGL2 renderer.
 - Fallback fonts should fail less on Linux.

10.0.4 - 2019-05-17
-------------------
Changed
 - Now depends on cffi 0.12 or later.

Fixed
 - `tcod.console_init_root` and `tcod.console_set_custom_font` will raise
   exceptions instead of terminating.
 - Fixed issues preventing `tcod.event` from working on 32-bit Windows.

10.0.3 - 2019-05-10
-------------------
Fixed
 - Corrected bounding box issues with the `Console.print_box` method.

10.0.2 - 2019-04-26
-------------------
Fixed
 - Resolved Color warnings when importing tcod.
 - When compiling, fixed a name conflict with endianness macros on FreeBSD.

10.0.1 - 2019-04-19
-------------------
Fixed
 - Fixed horizontal alignment for TrueType fonts.
 - Fixed taking screenshots with the older SDL renderer.

10.0.0 - 2019-03-29
-------------------
Added
 - New `Console.tiles` array attribute.
Changed
 - `Console.DTYPE` changed to add alpha to its color types.
Fixed
 - Console printing was ignoring color codes at the beginning of a string.

9.3.0 - 2019-03-15
------------------
Added
 - The SDL2/OPENGL2 renderers can potentially use a fall-back font when none
   are provided.
 - New function `tcod.event.get_mouse_state`.
 - New function `tcod.map.compute_fov` lets you get a visibility array directly
   from a transparency array.
Deprecated
 - The following functions and classes have been deprecated.
   - `tcod.Key`
   - `tcod.Mouse`
   - `tcod.mouse_get_status`
   - `tcod.console_is_window_closed`
   - `tcod.console_check_for_keypress`
   - `tcod.console_wait_for_keypress`
   - `tcod.console_delete`
   - `tcod.sys_check_for_event`
   - `tcod.sys_wait_for_event`
 - The SDL, OPENGL, and GLSL renderers have been deprecated.
 - Many libtcodpy functions have been marked with PendingDeprecationWarning's.
Fixed
 - To be more compatible with libtcodpy `tcod.console_init_root` will default
   to the SDL render, but will raise warnings when an old renderer is used.

9.2.5 - 2019-03-04
------------------
Fixed
 - Fixed `tcod.namegen_generate_custom`.

9.2.4 - 2019-03-02
------------------
Fixed
 - The `tcod` package is has been marked as typed and will now work with MyPy.

9.2.3 - 2019-03-01
------------------
Deprecated
 - The behavior for negative indexes on the new print functions may change in
   the future.
 - Methods and functionality preventing `tcod.Color` from behaving like a tuple
   have been deprecated.

9.2.2 - 2019-02-26
------------------
Fixed
 - `Console.print_box` wasn't setting the background color by default.

9.2.1 - 2019-02-25
------------------
Fixed
 - `tcod.sys_get_char_size` fixed on the new renderers.

9.2.0 - 2019-02-24
------------------
Added
 - New `tcod.console.get_height_rect` function, which can be used to get the
   height of a print call without an existing console.
 - New `tcod.tileset` module, with a `set_truetype_font` function.
Fixed
 - The new print methods now handle alignment according to how they were
   documented.
 - `SDL2` and `OPENGL2` now support screenshots.
 - Windows and MacOS builds now restrict exported SDL2 symbols to only
   SDL 2.0.5;  This will avoid hard to debug import errors when the wrong
   version of SDL is dynamically linked.
 - The root console now starts with a white foreground.

9.1.0 - 2019-02-23
------------------
Added
 - Added the `tcod.random.MULTIPLY_WITH_CARRY` constant.
Changed
 - The overhead for warnings has been reduced when running Python with the
   optimize `-O` flag.
 - `tcod.random.Random` now provides a default algorithm.

9.0.0 - 2019-02-17
------------------
Changed
 - New console methods now default to an `fg` and `bg` of None instead of
   white-on-black.

8.5.0 - 2019-02-15
------------------
Added
 - `tcod.console.Console` now supports `str` and `repr`.
 - Added new Console methods which are independent from the console defaults.
 - You can now give an array when initializing a `tcod.console.Console`
   instance.
 - `Console.clear` can now take `ch`, `fg`, and `bg` parameters.
Changed
 - Updated libtcod to 1.10.6
 - Printing generates more compact layouts.
Deprecated
 - Most libtcodpy console functions have been replaced by the tcod.console
   module.
 - Deprecated the `set_key_color` functions.  You can pass key colors to
   `Console.blit` instead.
 - `Console.clear` should be given the colors to clear with as parameters,
   rather than by using `default_fg` or `default_bg`.
 - Most functions which depend on console default values have been deprecated.
   The new deprecation warnings will give details on how to make default values
   explicit.
Fixed
 - `tcod.console.Console.blit` was ignoring the key color set by
   `Console.set_key_color`.
 - The `SDL2` and `OPENGL2` renders can now large numbers of tiles.

8.4.3 - 2019-02-06
------------------
Changed
 - Updated libtcod to 1.10.5
 - The SDL2/OPENGL2 renderers will now auto-detect a custom fonts key-color.

8.4.2 - 2019-02-05
------------------
Deprecated
 - The tdl module has been deprecated.
 - The libtcodpy parser functions have been deprecated.
Fixed
 - `tcod.image_is_pixel_transparent` and `tcod.image_get_alpha` now return
   values.
 - `Console.print_frame` was clearing tiles outside if its bounds.
 - The `FONT_LAYOUT_CP437` layout was incorrect.

8.4.1 - 2019-02-01
------------------
Fixed
 - Window event types were not upper-case.
 - Fixed regression where libtcodpy mouse wheel events unset mouse coordinates.

8.4.0 - 2019-01-31
------------------
Added
 - Added tcod.event module, based off of the sdlevent.py shim.
Changed
 - Updated libtcod to 1.10.3
Fixed
 - Fixed libtcodpy `struct_add_value_list` function.
 - Use correct math for tile-based delta in mouse events.
 - New renderers now support tile-based mouse coordinates.
 - SDL2 renderer will now properly refresh after the window is resized.

8.3.2 - 2018-12-28
------------------
Fixed
 - Fixed rare access violations for some functions which took strings as
   parameters, such as `tcod.console_init_root`.

8.3.1 - 2018-12-28
------------------
Fixed
 - libtcodpy key and mouse functions will no longer accept the wrong types.
 - The `new_struct` method was not being called for libtcodpy's custom parsers.

8.3.0 - 2018-12-08
------------------
Added
 - Added BSP traversal methods in tcod.bsp for parity with libtcodpy.
Deprecated
 - Already deprecated bsp functions are now even more deprecated.

8.2.0 - 2018-11-27
------------------
Added
 - New layout `tcod.FONT_LAYOUT_CP437`.
Changed
 - Updated libtcod to 1.10.2
 - `tcod.console_print_frame` and `Console.print_frame` now support Unicode
   strings.
Deprecated
 - Deprecated using bytes strings for all printing functions.
Fixed
 - Console objects are now initialized with spaces. This fixes some blit
   operations.
 - Unicode code-points above U+FFFF will now work on all platforms.

8.1.1 - 2018-11-16
------------------
Fixed
 - Printing a frame with an empty string no longer displays a title bar.

8.1.0 - 2018-11-15
------------------
Changed
 - Heightmap functions now support 'F_CONTIGUOUS' arrays.
 - `tcod.heightmap_new` now has an `order` parameter.
 - Updated SDL to 2.0.9
Deprecated
 - Deprecated heightmap functions which sample noise grids, this can be done
   using the `Noise.sample_ogrid` method.

8.0.0 - 2018-11-02
------------------
Changed
 - The default renderer can now be anything if not set manually.
 - Better error message for when a font file isn't found.

7.0.1 - 2018-10-27
------------------
Fixed
 - Building from source was failing because `console_2tris.glsl*` was missing
   from source distributions.

7.0.0 - 2018-10-25
------------------
Added
 - New `RENDERER_SDL2` and `RENDERER_OPENGL2` renderers.
Changed
 - Updated libtcod to 1.9.0
 - Now requires SDL 2.0.5, which is not trivially installable on
   Ubuntu 16.04 LTS.
Removed
 - Dropped support for Python versions before 3.5
 - Dropped support for MacOS versions before 10.9 Mavericks.

6.0.7 - 2018-10-24
------------------
Fixed
 - The root console no longer loses track of buffers and console defaults on a
   renderer change.

6.0.6 - 2018-10-01
------------------
Fixed
 - Replaced missing wheels for older and 32-bit versions of MacOS.

6.0.5 - 2018-09-28
------------------
Fixed
 - Resolved CDefError error during source installs.

6.0.4 - 2018-09-11
------------------
Fixed
 - tcod.Key right-hand modifiers are now set independently at initialization,
   instead of mirroring the left-hand modifier value.

6.0.3 - 2018-09-05
------------------
Fixed
 - tcod.Key and tcod.Mouse no longer ignore initiation parameters.

6.0.2 - 2018-08-28
------------------
Fixed
 - Fixed color constants missing at build-time.

6.0.1 - 2018-08-24
------------------
Fixed
 - Source distributions were missing C++ source files.

6.0.0 - 2018-08-23
------------------
Changed
 - Project renamed to tcod on PyPI.
Deprecated
 - Passing bytes strings to libtcodpy print functions is deprecated.
Fixed
 - Fixed libtcodpy print functions not accepting bytes strings.
 - libtcod constants are now generated at build-time fixing static analysis
   tools.

5.0.1 - 2018-07-08
------------------
Fixed
 - tdl.event no longer crashes with StopIteration on Python 3.7

5.0.0 - 2018-07-05
------------------
Changed
 - tcod.path: all classes now use `shape` instead of `width` and `height`.
 - tcod.path now respects NumPy array shape, instead of assuming that arrays
   need to be transposed from C memory order.  From now on `x` and `y` mean
   1st and 2nd axis.  This doesn't affect non-NumPy code.
 - tcod.path now has full support of non-contiguous memory.

4.6.1 - 2018-06-30
------------------
Added
 - New function `tcod.line_where` for indexing NumPy arrays using a Bresenham
   line.
Deprecated
 - Python 2.7 support will be dropped in the near future.

4.5.2 - 2018-06-29
------------------
Added
 - New wheels for Python3.7 on Windows.
Fixed
 - Arrays from `tcod.heightmap_new` are now properly zeroed out.

4.5.1 - 2018-06-23
------------------
Deprecated
 - Deprecated all libtcodpy map functions.
Fixed
 - `tcod.map_copy` could break the `tcod.map.Map` class.
 - `tcod.map_clear` `transparent` and `walkable` parameters were reversed.
 - When multiple SDL2 headers were installed, the wrong ones would be used when
   the library is built.
 - Fails to build via pip unless Numpy is installed first.

4.5.0 - 2018-06-12
------------------
Changed
 - Updated libtcod to v1.7.0
 - Updated SDL to v2.0.8
 - Error messages when failing to create an SDL window should be a less vague.
 - You no longer need to initialize libtcod before you can print to an
   off-screen console.
Fixed
 - Avoid crashes if the root console has a character code higher than expected.
Removed
 - No more debug output when loading fonts.

4.4.0 - 2018-05-02
------------------
Added
 - Added the libtcodpy module as an alias for tcod.  Actual use of it is
   deprecated, it exists primarily for backward compatibility.
 - Adding missing libtcodpy functions `console_has_mouse_focus` and
   `console_is_active`.
Changed
 - Updated libtcod to v1.6.6

4.3.2 - 2018-03-18
------------------
Deprecated
 - Deprecated the use of falsy console parameters with libtcodpy functions.
Fixed
 - Fixed libtcodpy image functions not supporting falsy console parameters.
 - Fixed tdl `Window.get_char` method. (Kaczor2704)

4.3.1 - 2018-03-07
------------------
Fixed
 - Fixed cffi.api.FFIError "unsupported expression: expected a simple numeric
   constant" error when building on platforms with an older cffi module and
   newer SDL headers.
 - tcod/tdl Map and Console objects were not saving stride data when pickled.

4.3.0 - 2018-02-01
------------------
Added
 - You can now set the numpy memory order on tcod.console.Console,
   tcod.map.Map, and tdl.map.Map objects well as from the
   tcod.console_init_root function.
Changed
 - The `console_init_root` `title` parameter is now optional.
Fixed
 - OpenGL renderer alpha blending is now consistent with all other render
   modes.

4.2.3 - 2018-01-06
------------------
Fixed
 - Fixed setup.py regression that could prevent building outside of the git
   repository.

4.2.2 - 2018-01-06
------------------
Fixed
 - The Windows dynamic linker will now prefer the bundled version of SDL.
   This fixes:
   "ImportError: DLL load failed: The specified procedure could not be found."
 - `key.c` is no longer set when `key.vk == KEY_TEXT`, this fixes a regression
   which was causing events to be heard twice in the libtcod/Python tutorial.

4.2.0 - 2018-01-02
------------------
Changed
 - Updated libtcod backend to v1.6.4
 - Updated SDL to v2.0.7 for Windows/MacOS.
Removed
 - Source distributions no longer include tests, examples, or fonts.
   `Find these on GitHub. <https://github.com/HexDecimal/python-tdl>`_
Fixed
 - Fixed "final link failed: Nonrepresentable section on output" error
   when compiling for Linux.
 - `tcod.console_init_root` defaults to the SDL renderer, other renderers
   cause issues with mouse movement events.

4.1.1 - 2017-11-02
------------------
Fixed
 - Fixed `ConsoleBuffer.blit` regression.
 - Console defaults corrected, the root console's blend mode and alignment is
   the default value for newly made Console's.
 - You can give a byte string as a filename to load parsers.

4.1.0 - 2017-07-19
------------------
Added
 - tdl Map class can now be pickled.
Changed
 - Added protection to the `transparent`, `walkable`, and `fov`
   attributes in tcod and tdl Map classes, to prevent them from being
   accidentally overridden.
 - tcod and tdl Map classes now use numpy arrays as their attributes.

4.0.1 - 2017-07-12
------------------
Fixed
 - tdl: Fixed NameError in `set_fps`.

4.0.0 - 2017-07-08
------------------
Changed
 - tcod.bsp: `BSP.split_recursive` parameter `random` is now `seed`.
 - tcod.console: `Console.blit` parameters have been rearranged.
   Most of the parameters are now optional.
 - tcod.noise: `Noise.__init__` parameter `rand` is now named `seed`.
 - tdl: Changed `set_fps` paramter name to `fps`.
Fixed
 - tcod.bsp: Corrected spelling of max_vertical_ratio.

3.2.0 - 2017-07-04
------------------
Changed
 - Merged libtcod-cffi dependency with TDL.
Fixed
 - Fixed boolean related crashes with Key 'text' events.
 - tdl.noise: Fixed crash when given a negative seed.  As well as cases
   where an instance could lose its seed being pickled.

3.1.0 - 2017-05-28
------------------
Added
 - You can now pass tdl Console instances as parameters to libtcod-cffi
   functions expecting a tcod Console.
Changed
 - Dependencies updated: `libtcod-cffi>=2.5.0,<3`
 - The `Console.tcod_console` attribute is being renamed to
   `Console.console_c`.
Deprecated
 - The tdl.noise and tdl.map modules will be deprecated in the future.
Fixed
 - Resolved crash-on-exit issues for Windows platforms.

3.0.2 - 2017-04-13
------------------
Changed
 - Dependencies updated: `libtcod-cffi>=2.4.3,<3`
 - You can now create Console instances before a call to `tdl.init`.
Removed
 - Dropped support for Python 3.3
Fixed
 - Resolved issues with MacOS builds.
 - 'OpenGL' and 'GLSL' renderers work again.

3.0.1 - 2017-03-22
------------------
Changed
 - `KeyEvent`'s with `text` now have all their modifier keys set to False.
Fixed
 - Undefined behaviour in text events caused crashes on 32-bit builds.

3.0.0 - 2017-03-21
------------------
Added
 - `KeyEvent` supports libtcod text and meta keys.
Changed
 - `KeyEvent` parameters have been moved.
 - This version requires `libtcod-cffi>=2.3.0`.
Deprecated
 - `KeyEvent` camel capped attribute names are deprecated.
Fixed
 - Crashes with key-codes undefined by libtcod.
 - `tdl.map` typedef issues with libtcod-cffi.


2.0.1 - 2017-02-22
------------------
Fixed
 - `tdl.init` renderer was defaulted to OpenGL which is not supported in the
   current version of libtcod.

2.0.0 - 2017-02-15
------------------
Changed
 - Dependencies updated, tdl now requires libtcod-cffi 2.x.x
 - Some event behaviours have changed with SDL2, event keys might be different
   than what you expect.
Removed
 - Key repeat functions were removed from SDL2.
   `set_key_repeat` is now stubbed, and does nothing.

1.6.0 - 2016-11-18
------------------
- Console.blit methods can now take fg_alpha and bg_alpha parameters.

1.5.3 - 2016-06-04
------------------
- set_font no longer crashes when loading a file without the implied font
  size in its name

1.5.2 - 2016-03-11
------------------
- Fixed non-square Map instances

1.5.1 - 2015-12-20
------------------
- Fixed errors with Unicode and non-Unicode literals on Python 2
- Fixed attribute error in compute_fov

1.5.0 - 2015-07-13
------------------
- python-tdl distributions are now universal builds
- New Map class
- map.bresenham now returns a list
- This release will require libtcod-cffi v0.2.3 or later

1.4.0 - 2015-06-22
------------------
- The DLL's have been moved into another library which you can find at
  https://github.com/HexDecimal/libtcod-cffi
  You can use this library to have some raw access to libtcod if you want.
  Plus it can be used alongside TDL.
- The libtocd console objects in Console instances have been made public.
- Added tdl.event.wait function.  This function can called with a timeout and
  can automatically call tdl.flush.

1.3.1 - 2015-06-19
------------------
- Fixed pathfinding regressions.

1.3.0 - 2015-06-19
------------------
- Updated backend to use python-cffi instead of ctypes.  This gives decent
  boost to speed in CPython and a drastic to boost in speed in PyPy.

1.2.0 - 2015-06-06
------------------
- The set_colors method now changes the default colors used by the draw_*
  methods.  You can use Python's Ellipsis to explicitly select default colors
  this way.
- Functions and Methods renamed to match Python's style-guide PEP 8, the old
  function names still exist and are depreciated.
- The fgcolor and bgcolor parameters have been shortened to fg and bg.

1.1.7 - 2015-03-19
------------------
- Noise generator now seeds properly.
- The OS event queue will now be handled during a call to tdl.flush. This
  prevents a common newbie programmer hang where events are handled
  infrequently during long animations, simulations, or early development.
- Fixed a major bug that would cause a crash in later versions of Python 3

1.1.6 - 2014-06-27
------------------
- Fixed a race condition when importing on some platforms.
- Fixed a type issue with quickFOV on Linux.
- Added a bresenham function to the tdl.map module.

1.1.5 - 2013-11-10
------------------
- A for loop can iterate over all coordinates of a Console.
- drawStr can be configured to scroll or raise an error.
- You can now configure or disable key repeating with tdl.event.setKeyRepeat
- Typewriter class removed, use a Window instance for the same functionality.
- setColors method fixed.

1.1.4 - 2013-03-06
------------------
- Merged the Typewriter and MetaConsole classes,
  You now have a virtual cursor with Console and Window objects.
- Fixed the clear method on the Window class.
- Fixed screenshot function.
- Fixed some drawing operations with unchanging backgrounds.
- Instances of Console and Noise can be pickled and copied.
- Added KeyEvent.keychar
- Fixed event.keyWait, and now converts window closed events into Alt+F4.

1.1.3 - 2012-12-17
------------------
- Some of the setFont parameters were incorrectly labeled and documented.
- setFont can auto-detect tilesets if the font sizes are in the filenames.
- Added some X11 unicode tilesets, including unifont.

1.1.2 - 2012-12-13
------------------
- Window title now defaults to the running scripts filename.
- Fixed incorrect deltaTime for App.update
- App will no longer call tdl.flush on its own, you'll need to call this
  yourself.
- tdl.noise module added.
- clear method now defaults to black on black.

1.1.1 - 2012-12-05
------------------
- Map submodule added with AStar class and quickFOV function.
- New Typewriter class.
- Most console functions can use Python-style negative indexes now.
- New App.runOnce method.
- Rectangle geometry is less strict.

1.1.0 - 2012-10-04
------------------
- KeyEvent.keyname is now KeyEvent.key
- MouseButtonEvent.button now behaves like KeyEvent.keyname does.
- event.App class added.
- Drawing methods no longer have a default for the character parameter.
- KeyEvent.ctrl is now KeyEvent.control

1.0.8 - 2010-04-07
------------------
- No longer works in Python 2.5 but now works in 3.x and has been partly
  tested.
- Many bug fixes.

1.0.5 - 2010-04-06
------------------
- Got rid of setuptools dependency, this will make it much more compatible
  with Python 3.x
- Fixed a typo with the MacOS library import.

1.0.4 - 2010-04-06
------------------
- All constant colors (C_*) have been removed, they may be put back in later.
- Made some type assertion failures show the value they received to help in
  general debugging.  Still working on it.
- Added MacOS and 64-bit Linux support.

1.0.0 - 2009-01-31
------------------
- First public release.
