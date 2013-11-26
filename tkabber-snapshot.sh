#!/bin/sh

version=0.11.1
svnrev=1948

svn export -r $svnrev http://svn.xmpp.ru/repos/tkabber/trunk/tkabber tkabber-${version}

tar cjf tkabber-${version}.tar.bz2 tkabber-${version}
