package main

import "errors"

// Node represents a node in the doubly linked list
type Node struct {
	url  string
	prev *Node
	next *Node
}

// BrowserHistory manages the browsing history using a doubly linked list
type BrowserHistory struct {
	current *Node
}

// NewBrowserHistory initializes a new BrowserHistory instance
func NewBrowserHistory() *BrowserHistory {
	return &BrowserHistory{}
}

// VisitNewPage adds a new page to the history
func (bh *BrowserHistory) VisitNewPage(url string) {
	newNode := &Node{url: url}

	if bh.current != nil {
		// If we're not at the tail, clear the forward history
		if bh.current.next != nil {
			bh.current.next = nil // Discard forward pages
		}
	} else {
		// If the history is empty, initialize the current node
		bh.current = newNode
		return
	}

	// Add the new page at the end of the history
	newNode.prev = bh.current
	bh.current.next = newNode
	bh.current = newNode
}

// Back moves to the previous page in the history
func (bh *BrowserHistory) Back() error {
	if bh.current == nil || bh.current.prev == nil {
		return errors.New("no previous page")
	}
	bh.current = bh.current.prev
	return nil
}

// Forward moves to the next page in the history
func (bh *BrowserHistory) Forward() error {
	if bh.current == nil || bh.current.next == nil {
		return errors.New("no next page")
	}
	bh.current = bh.current.next
	return nil
}

// ClearHistory clears the entire history
func (bh *BrowserHistory) ClearHistory() {
	bh.current = nil
}

// GetCurrentURL returns the current page URL
func (bh *BrowserHistory) GetCurrentURL() string {
	if bh.current == nil {
		return ""
	}
	return bh.current.url
}
