AM_CFLAGS = \
	-Wall

AM_CPPFLAGS = \
	@PYTHON_CPPFLAGS@ \
	-include Python.h

AM_CXXFLAGS = \
	-Wall \
	@ENIGMA2_CFLAGS@

plugindir = $(libdir)/enigma2/python/Plugins/SystemPlugins/Servicelibpl

plugin_LTLIBRARIES = servicelibpl.la

servicelibpl_la_SOURCES = \
	pythonmodule.cpp \
	servicelibpl.cpp \
	m3u8.cpp

servicelibpl_la_LDFLAGS = \
	-avoid-version \
	-module \
	-shared \
        -leplayer3
