
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	locations := make(map[string][2]int) // Store locations
	var order []string                   // Store order of locations
	var unresolved [][]string            // Unresolved locations

	// Read the first line - start -
	if scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) != 3 || !strings.HasPrefix(parts[1], "x=") || !strings.HasPrefix(parts[2], "y=") {
			return
		}

		startXStr := strings.TrimPrefix(parts[1], "x=")
		startYStr := strings.TrimPrefix(parts[2], "y=")

		startX, err1 := strconv.Atoi(startXStr)
		startY, err2 := strconv.Atoi(startYStr)
		if err1 != nil || err2 != nil {
			return
		}
		locations["start"] = [2]int{startX, startY}
	}

	// Read the rest of the lines
	for scanner.Scan() {
		line := scanner.Text()
		// Check for an empty line to terminate input
		if strings.TrimSpace(line) == "" {
			break
		}

		parts := strings.Fields(line)
		if len(parts) != 5 || !strings.HasPrefix(parts[3], "x=") || !strings.HasPrefix(parts[4], "y=") {
			continue
		}

		name := parts[0]        // New location name
		destination := parts[2] // Reference location name

		// Separate x and y
		dxStr := strings.TrimPrefix(parts[3], "x=")
		dyStr := strings.TrimPrefix(parts[4], "y=")

		dx, err1 := strconv.Atoi(dxStr)
		dy, err2 := strconv.Atoi(dyStr)
		if err1 != nil || err2 != nil {
			continue
		}

		// Check if the destination is already known
		refCoord, ok := locations[destination]
		if !ok {
			// If the destination is not yet resolved, save it as unresolved
			unresolved = append(unresolved, parts)
			order = append(order, name) // Append to order
			continue
		}

		// New coordinates
		newX := refCoord[0] + dx
		newY := refCoord[1] + dy

		// Save the new location's coordinates
		locations[name] = [2]int{newX, newY}
		order = append(order, name) // Append to order
	}

	// Resolve unresolved locations
	resolveUnresolved(locations, &unresolved)

	// Print results excluding the "start" location
	for _, name := range order {
		if name != "start" { // Skip printing "start"
			if coords, ok := locations[name]; ok {
				fmt.Printf("%s x=%d y=%d\n", name, coords[0], coords[1])
			}
		}
	}
}

// resolveUnresolved tries to resolve unresolved locations
func resolveUnresolved(locations map[string][2]int, unresolved *[][]string) {
	if len(*unresolved) == 0 {
		return // Exit if there are no unresolved locations
	}

	var temp [][]string // Temporarily hold unresolved locations

	for _, parts := range *unresolved {
		name := parts[0]        // New location name
		destination := parts[2] // Reference location name

		dxStr := strings.TrimPrefix(parts[3], "x=")
		dyStr := strings.TrimPrefix(parts[4], "y=")

		dx, _ := strconv.Atoi(dxStr)
		dy, _ := strconv.Atoi(dyStr)

		// Check destination integrity
		refCoord, ok := locations[destination]
		if !ok {
			// If destination still not found, keep it unresolved
			temp = append(temp, parts)
			continue
		}

		// New coordinates
		newX := refCoord[0] + dx
		newY := refCoord[1] + dy

		// Save new location's coordinates
		locations[name] = [2]int{newX, newY}
	}

	// Update unresolved locations
	*unresolved = temp

	// Recursive call
	resolveUnresolved(locations, unresolved)
}


