#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/yfinance
#
# Copyright 2017-2019 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__version__ = "0.1.56"
__author__ = "Ran Aroussi"

from .ticker import Ticker
from .tickers import Tickers
from .multi import download


def pdr_override():
    """
    make pandas datareader optional
    otherwise can be called via fix_yahoo_finance.download(...)
    """
    try:
        import pandas_datareader
        pandas_datareader.data.get_data_yahoo = download
        pandas_datareader.data.get_data_yahoo_actions = download
        pandas_datareader.data.DataReader = download
    except Exception:
        pass


__all__ = ['download', 'Ticker', 'Tickers', 'pdr_override']
