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
	[  --enable-libeplayer3          enable TDT libeplayer3 as player engine support],
[case "${enableval}" in
	yes) libeplayer3=true ;;
	no)  libeplayer3=false ;;
	*) AC_MSG_ERROR([bad value ${enableval} for --enable-libeplayer3]) ;;
esac],[libeplayer3=false])
AM_CONDITIONAL(ENABLE_LIBEPLAYER3, [test x$libeplayer3 = xtrue])
if test "$enable_libeplayer3" = "yes"; then
	AC_DEFINE(ENABLE_LIBEPLAYER3, 1 ,[include TDT libeplayer3 as player engine support])
#	PKG_CHECK_MODULES(BASE, [freetype2 fribidi libdvbsi++ libpng libxml-2.0 sigc++-2.0 libssl libcrypto])
	PKG_CHECK_MODULES([AVFORMAT], [libavformat >= 53.21.1])
	PKG_CHECK_MODULES([AVCODEC], [libavcodec >= 54.28.0])
	# do not know which version is exactly needed here...
	PKG_CHECK_MODULES([AVUTIL], [libavutil])
	PKG_CHECK_MODULES([SWSCALE], [libswscale])
	PKG_CHECK_MODULES([SWRESAMPLE], [libswresample])
fi

AC_ARG_ENABLE([gstreamer],
	[  --enable-gstreamer            enable gstreamer as player engine support],
[case "${enableval}" in
	yes) gstreamer=true ;;
	no)  gstreamer=false ;;
	*) AC_MSG_ERROR([bad value ${enableval} for --enable-gstreamer]) ;;
esac],[gstreamer=false])
AM_CONDITIONAL(ENABLE_GSTREAMER, [test x$gstreamer = xtrue])
if test "$enable_gstreamer" = "yes"; then
	AC_DEFINE(ENABLE_GSTREAMER, 1 ,[include gstreamer as player engine support])
#	AC_ARG_WITH(gstversion,
#		AS_HELP_STRING([--with-gstversion],[use gstreamer version (major.minor)]),
#		[GST_MAJORMINOR=$withval],[GST_MAJORMINOR=1.0])
#	PKG_CHECK_MODULES(GSTREAMER, gstreamer-$GST_MAJORMINOR gstreamer-pbutils-$GST_MAJORMINOR)
	PKG_CHECK_MODULES(GSTREAMER, gstreamer-1.0 gstreamer-pbutils-1.0)
#	PKG_CHECK_MODULES(BASE, [freetype2 fribidi gstreamer-$GST_MAJORMINOR gstreamer-pbutils-$GST_MAJORMINOR libdvbsi++ libpng libxml-2.0 sigc++-2.0 libssl libcrypto])
	PKG_CHECK_MODULES(BASE, [freetype2 fribidi gstreamer-1.0 gstreamer-pbutils-1.0 libdvbsi++ libpng libxml-2.0 sigc++-2.0 libssl libcrypto])
else
	PKG_CHECK_MODULES(BASE, [freetype2 fribidi libdvbsi++ libpng libxml-2.0 sigc++-2.0 libssl libcrypto])
fi

AC_ARG_ENABLE([dual_mediafw],
	[  --enable-dual_mediafw          enable selectable media framework as player engine support],
[case "${enableval}" in
	yes) dualmediafw=true ;;
	no)  dualmediafw=false ;;
	*) AC_MSG_ERROR([bad value ${enableval} for --enable-dual_mediafw]) ;;
esac],[dualmediafw=false])
AM_CONDITIONAL(ENABLE_DUAL_MEDIAFW, [test x$dualmediafw = xtrue])
if test "$enable_dual_mediafw" = "yes"; then
	AC_DEFINE(ENABLE_DUAL_MEDIAFW, 1 ,[include selectable media framework as player engine support])
	PKG_CHECK_MODULES(GSTREAMER, gstreamer-1.0 gstreamer-pbutils-1.0)
	PKG_CHECK_MODULES(BASE, [freetype2 fribidi gstreamer-1.0 gstreamer-pbutils-1.0 libdvbsi++ libpng libxml-2.0 sigc++-2.0 libssl libcrypto])
	PKG_CHECK_MODULES([AVFORMAT], [libavformat >= 53.21.1])
	PKG_CHECK_MODULES([AVCODEC], [libavcodec >= 54.28.0])
	# do not know which version is exactly needed here...
	PKG_CHECK_MODULES([AVUTIL], [libavutil])
	PKG_CHECK_MODULES([SWSCALE], [libswscale])
	PKG_CHECK_MODULES([SWRESAMPLE], [libswresample])
fi

AC_DEFINE([DEBUG])

AC_CONFIG_FILES([
Makefile
servicemp3/Makefile
plugin/Makefile
])
AC_OUTPUT
