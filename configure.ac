AC_INIT([servicelibpl], [0.1], [])
AM_INIT_AUTOMAKE([subdir-objects foreign dist-bzip2 no-define tar-pax])
AC_CONFIG_MACRO_DIR([m4])
LT_INIT

AC_PROG_CC
AC_PROG_CXX
AM_PATH_PYTHON
AX_PYTHON_DEVEL
AC_LANG(C++)

PKG_CHECK_MODULES(ENIGMA2, enigma2)

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

AC_ARG_WITH(binarycompatibledebug,
	AC_HELP_STRING([--with-binarycompatibledebug], [use e2 independent debug output]),
	[[with_binarycompatibledebug=$withval]],
	[[with_binarycompatibledebug=no]]
)

if test x"$with_binarycompatibledebug" = xyes ; then
	AC_DEFINE([BINARY_COMPATIBLE_DEBUGLOG])
fi

AC_CONFIG_FILES([
Makefile
servicelibpl/Makefile
plugin/Makefile
])
AC_OUTPUT
