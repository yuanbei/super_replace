#!/bin/sh
python replace.py -i ../superadb/src/org -s "package org.adblockplus.android;" -r "#if !defined(WOW_BUILD)
package org.adblockplus.android;
#else
package com.superadb.android;
#endif" -e exclude.txt
