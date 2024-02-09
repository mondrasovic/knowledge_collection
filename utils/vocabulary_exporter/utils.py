from __future__ import annotations

import datetime
from urllib.parse import quote, urlparse, urlunparse


def encode_url(url: str) -> str:
    parsed_url = urlparse(url)
    encoded_path = quote(parsed_url.path)
    encoded_query = quote(parsed_url.query)

    # Combine the encoded parts back into a URL
    encoded_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            encoded_path,
            parsed_url.params,
            encoded_query,
            parsed_url.fragment,
        )
    )

    return encoded_url


def get_current_month_name() -> str:
    return datetime.datetime.now().strftime("%B")

