
# Browser History Simulation

Since entering Snap, X promised himself to work on algorithm practice and data structure daily. This time, X wants to simulate his browser history using a linked list.

## Program Requirements

1. The system should add new web pages that X visits to the history.
2. The system should allow X to move backward or forward in the browser history.
3. If X visits a new page while in the middle of the history (not on the most recently visited page), the system should remove all forward pages and add the new page to the end of the history.
4. The system should clear the entire browser history and reset to the initial state.
5. X should be able to get the URL of the current page he is viewing.

## Implementation Tasks

### Structures and Methods to Implement

#### Type `BrowserHistory`

You need to create a `BrowserHistory` structure that maintains all the necessary data to manage browser history. You can add additional fields to this struct.

#### Function `NewBrowserHistory`

This function initiXzes and returns an instance of `BrowserHistory`.

#### Method `VisitNewPage`

This method should add a new page to the history. If the user is in the middle of the history, all forward pages should be removed, and the new page should be added to the end of the history.

#### Method `Back`

This method should move the user to the previous page in the history. If at the beginning of the history, it should return an error `no previous page`.

#### Method `Forward`

This method should move the user to the next page in the history. If at the end of the history, it should return an error `no next page`.

#### Method `ClearHistory`

This method should clear the entire browser history and reset the system to its initial state.

#### Method `GetCurrentURL`

This method should return the URL of the current page being viewed by the user.

### Additional Notes

- Use a doubly linked list to implement this system and ensure that all operations are implemented efficiently.
- Do not change any of the initial project structures (function signatures and struct fields). Otherwise, the tests will not pass.
