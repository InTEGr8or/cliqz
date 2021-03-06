# coding=utf-8
"""DuckDuckGo Instant Answer API feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\quiz.feature', 'Basic DuckDuckGo API Query')
def test_basic_duckduckgo_api_query():
    """Basic DuckDuckGo API Query."""


@given('the DuckDuckGo API is queried with "<phrase>" using "json" format')
def the_duckduckgo_api_is_queried_with_phrase_using_json_format():
    """the DuckDuckGo API is queried with "<phrase>" using "json" format."""
    raise NotImplementedError


@then('the response contains results for "<phrase>"')
def the_response_contains_results_for_phrase():
    """the response contains results for "<phrase>"."""
    raise NotImplementedError


@then('the response status code is "200"')
def the_response_status_code_is_200():
    """the response status code is "200"."""
    raise NotImplementedError

