#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

import model.Monster

if __name__ == "__main__":
	m = model.Monster.Monster();
	m.get_charactor_info_from_url(203);
	raw_input();
