# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Pincer
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from pincer.utils.api_object import APIObject

from pincer.objects.user import User
from pincer.utils.constants import OptionallyProvided, MISSING


@dataclass
class Application(APIObject):
    bot_public: bool
    bot_require_code_grant: bool
    description: str
    id: int
    icon: Optional[str]
    name: str
    privacy_policy_url: OptionallyProvided[str]
    summary: str
    verify_key: str

    cover_image: OptionallyProvided[str] = MISSING
    flags: OptionallyProvided[int] = MISSING
    guild_id: OptionallyProvided[int] = MISSING
    owner: OptionallyProvided[User] = MISSING
    primary_sku_id: OptionallyProvided[int] = MISSING
    rpc_origins: OptionallyProvided[List[str]] = MISSING
    slug: OptionallyProvided[str] = MISSING
    terms_of_service_url: OptionallyProvided[str] = MISSING