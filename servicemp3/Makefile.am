AM_CFLAGS = \
	-Wall

AM_CPPFLAGS = \
	@PYTHON_CPPFLAGS@ \
	-include Python.h

if ENABLE_DUAL_MEDIAFW
AM_CPPFLAGS += \
        -I$(top_srcdir)/../../tools/libeplayer3/include
endif

if ENABLE_LIBEPLAYER3
AM_CPPFLAGS += \
        -I$(top_srcdir)/../../tools/libeplayer3/include
endif

AM_CXXFLAGS = \
	-Wall \
	@ENIGMA2_CFLAGS@

if ENABLE_DUAL_MEDIAFW
AM_CXXFLAGS += \
	@GSTREAMER_CFLAGS@
endif

if ENABLE_GSTREAMER
AM_CXXFLAGS += \
	@GSTREAMER_CFLAGS@
endif

plugindir = $(libdir)/enigma2/python/Plugins/SystemPlugins/ServiceMP3

plugin_LTLIBRARIES = servicemp3.la

servicemp3_la_SOURCES = \
	pythonmodule.cpp

if ENABLE_DUAL_MEDIAFW
servicemp3_la_SOURCES += \
	servicemp3.cpp \
	servicemp3record.cpp \
 	servicelibpl.cpp \
	m3u8.cpp
else
if ENABLE_GSTREAMER
servicemp3_la_SOURCES += \
	servicemp3.cpp \
	servicemp3record.cpp
endif

if ENABLE_LIBEPLAYER3
servicemp3_la_SOURCES += \
	servicelibpl.cpp \
	m3u8.cpp
endif
endif

servicemp3_la_LDFLAGS = \
	-avoid-version \
	-module \
	-shared

if ENABLE_DUAL_MEDIAFW
servicemp3_la_LDFLAGS += \
	@GSTREAMER_LIBS@ \
        -leplayer3
else
if ENABLE_GSTREAMER
servicemp3_la_LDFLAGS += \
	@GSTREAMER_LIBS@
endif

if ENABLE_LIBEPLAYER3
servicemp3_la_LDFLAGS += \
        -leplayer3
endif
endif
