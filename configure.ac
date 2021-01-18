AC_INIT([servicemp3], [0.1], [])
AM_INIT_AUTOMAKE([subdir-objects foreign dist-bzip2 no-define tar-pax])
AC_CONFIG_MACRO_DIR([m4])
LT_INIT

AC_PROG_CC
AC_PROG_CXX
AM_PATH_PYTHON
AX_PYTHON_DEVEL
AC_LANG(C++)

PKG_CHECK_MODULES(ENIGMA2, enigma2)

AC_ARG_ENABLE([libeplayer3],
	[AS_HELP_STRING([--enable-libeplayer3],[enable libeplayer3 as player engine supportt])],
	[enable_libeplayer3=$enableval],
	[enable_libeplayer3=yes])

AM_CONDITIONAL(ENABLE_LIBEPLAYER3, test "$enable_libeplayer3" = "yes")

if test "$enable_libeplayer3" = "yes"; then
	AC_DEFINE(ENABLE_LIBEPLAYER3, 1, [include libeplayer3 as player engine support])
fi

AC_ARG_ENABLE([gstreamer],
	[AS_HELP_STRING([--enable-gstreamer],[enable gstreamer as player engine supportt])],
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

AC_ARG_WITH(boxtype,
	AS_HELP_STRING([--with-boxtype],[build for BOXTYPE, $withval]),
	[BOXTYPE="$withval"],[BOXTYPE=""])
AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AC_ARG_WITH(boxbrand,
	AS_HELP_STRING([--with-boxbrand],[build for BOXBRAND, $withval]),
	[BOXBRAND="$withval"],[BOXBRAND=""])
AC_SUBST(BOXBRAND)
AC_DEFINE_UNQUOTED(BOXBRAND,"$BOXBRAND",[box brand])

AC_ARG_WITH(stbplatform,
	AS_HELP_STRING([--with-stbplatform],[build for STBPLATFORM, $withval]),
	[STBPLATFORM="$withval"],[STBPLATFORM=""])
AC_SUBST(STBPLATFORM)
AC_DEFINE_UNQUOTED(STBPLATFORM,"$STBPLATFORM",[stb platform])

AC_DEFINE([DEBUG])

AC_CONFIG_FILES([
Makefile
servicemp3/Makefile
plugin/Makefile
])
AC_OUTPUT
