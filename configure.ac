AC_INIT([servicemp3epl], [0.1], [])
AM_INIT_AUTOMAKE([subdir-objects foreign dist-bzip2 no-define tar-pax])
AC_CONFIG_MACRO_DIR([m4])
LT_INIT

AC_PROG_CC
AC_PROG_CXX
AM_PATH_PYTHON
AX_PYTHON_DEVEL
AC_LANG(C++)

PKG_CHECK_MODULES(ENIGMA2, enigma2)

AC_ARG_ENABLE(libeplayer3,
	[  --enable-libeplayer3          enable TDT libeplayer3 as player engine supportt],
	[AC_DEFINE(ENABLE_LIBEPLAYER3, 1, [enable TDT libeplayer3 as player engine support])])
if test "$enable_libeplayer3" = "yes"; then
	AC_DEFINE(ENABLE_LIBEPLAYER3, 1, [include TDT libeplayer3 as player engine support])
fi

AM_CONDITIONAL(ENABLE_LIBEPLAYER3, test "$enable_libeplayer3" = "yes")

AC_ARG_ENABLE([gstreamer],
	[AS_HELP_STRING([--disable-gstreamer],[disable gstreamer as player engine supportt])],
	[enable_gstreamer=$enableval],
	[enable_gstreamer=yes])

AM_CONDITIONAL(ENABLE_GSTREAMER, test "$enable_gstreamer" = "yes")

if test "$enable_gstreamer" = "yes"; then
	AC_DEFINE(ENABLE_GSTREAMER, 1, [include gstreamer as player engine support])
	AC_ARG_WITH(gstversion,
		AS_HELP_STRING([--with-gstversion],[use gstreamer version (major.minor)]),
		[GST_MAJORMINOR=$withval],[GST_MAJORMINOR=1.0])
	PKG_CHECK_MODULES(GSTREAMER, gstreamer-$GST_MAJORMINOR gstreamer-pbutils-$GST_MAJORMINOR)
fi

AC_DEFINE([DEBUG])

AC_CONFIG_FILES([
Makefile
servicemp3epl/Makefile
plugin/Makefile
])
AC_OUTPUT
