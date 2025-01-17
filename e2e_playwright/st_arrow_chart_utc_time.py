# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
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

from datetime import date

import pandas as pd

import streamlit as st

df = pd.DataFrame(
    {
        "index": [
            date(2019, 8, 9),
            date(2019, 8, 10),
            date(2019, 8, 11),
            date(2019, 8, 12),
        ],
        "numbers": [10, 50, 30, 40],
    }
)

df.set_index("index", inplace=True)

# st.area/bar/line_chart all use Altair/Vega-Lite under the hood.
# By default, Vega-Lite displays time values in the browser's local
# time zone, but data is sent down to the browser as UTC. This means
# Times need to be set correctly to the users timezone.
st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
