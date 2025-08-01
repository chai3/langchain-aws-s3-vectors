"""Utilities for the Playwright browser tools."""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Tuple

if TYPE_CHECKING:
    from playwright.async_api import Browser as AsyncBrowser
    from playwright.async_api import Page as AsyncPage
    from playwright.sync_api import Browser as SyncBrowser
    from playwright.sync_api import Page as SyncPage


async def aget_current_page(browser: AsyncBrowser) -> AsyncPage:
    """
    Asynchronously get the current page of the browser.

    Args:
        browser: The browser (AsyncBrowser) to get the current page from.

    Returns:
        AsyncPage: The current page.
    """
    if not browser.contexts:
        context = await browser.new_context()
        return await context.new_page()
    context = browser.contexts[0]  # Assuming you're using the default browser context
    if not context.pages:
        return await context.new_page()
    # Assuming the last page in the list is the active one
    return context.pages[-1]


def get_current_page(browser: SyncBrowser) -> SyncPage:
    """
    Get the current page of the browser.
    Args:
        browser: The browser to get the current page from.

    Returns:
        SyncPage: The current page.
    """
    if not browser.contexts:
        context = browser.new_context()
        return context.new_page()
    context = browser.contexts[0]  # Assuming you're using the default browser context
    if not context.pages:
        return context.new_page()
    # Assuming the last page in the list is the active one
    return context.pages[-1]