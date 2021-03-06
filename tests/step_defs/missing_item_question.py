# coding=utf-8
"""Missing Item feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\missing_item_question.feature', 'Select a random item to omit')
def test_select_a_random_item_to_omit():
    """Select a random item to omit."""


@given('there are x=>range(2,7) valid items in the set')
def there_are_xrange27_valid_items_in_the_set():
    """there are x=>range(2,7) valid items in the set."""
    raise NotImplementedError


@when('I take the test')
def i_take_the_test():
    """I take the test."""
    raise NotImplementedError


@then('I should see x-1 items')
def i_should_see_x1_items():
    """I should see x-1 items."""
    raise NotImplementedError

