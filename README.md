markdown
# Astronomy MCP Server

## Overview

The Astronomy MCP Server is a robust platform designed to provide developers with easy access to a wealth of astronomical data. This server offers a suite of tools that enable the integration of celestial data into applications, providing a seamless interface for exploring and utilizing information from the skies.

## Features

- **Get All Bodies Positions**: Retrieve a comprehensive list of celestial bodies and their respective properties in a tabular format. This allows for detailed analysis and understanding of various celestial objects.
  
- **Get Positions for Body**: Obtain detailed properties of a specified celestial body over a defined date range. Supported bodies include the Sun, Moon, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto.
  
- **Search**: Utilize the search endpoint to fetch information about stars and deep space objects. This tool is particularly useful for astronomers and developers interested in specific celestial phenomena or objects.
  
- **Generate Moon Phase**: Create an image representing the current phase of the Moon based on specified parameters. This feature is ideal for educational purposes and applications focusing on lunar observations.
  
- **Generate Star Chart**: Produce a star chart with given parameters, allowing users to visualize the night sky as seen from a specific location and time. This tool is perfect for stargazers and educational applications to enhance the understanding of constellations and celestial events.

## Tool Details

### Get All Bodies Positions

- **Parameters**: Latitude, Longitude, Elevation (optional), From Date, To Date, Time (optional)
- **Description**: Returns a complete list of celestial bodies with properties such as position, visibility, and more.

### Get Positions for Body

- **Parameters**: Latitude, Longitude, Elevation (optional), From Date, To Date, Time (optional)
- **Description**: Provides detailed positional data for a selected celestial body over a specified timeframe.

### Search

- **Parameters**: Exact (optional), Match Type (options: exact, fuzzy), RA (Right Ascension), Dec (Declination), Limit (optional), Offset (optional), Order By (optional)
- **Description**: Search for stars and deep space objects based on various criteria and retrieve pertinent information.

### Generate Moon Phase

- **Parameters**: None
- **Description**: Generates a visual representation of the Moon's current phase.

### Generate Star Chart

- **Parameters**: None
- **Description**: Creates a star chart image based on specified parameters, providing a visual guide to the night sky.

## Conclusion

The Astronomy MCP Server is an invaluable resource for developers and astronomers alike, offering a comprehensive suite of tools to explore and integrate astronomical data into various applications. Whether you're interested in tracking celestial bodies, generating star charts, or learning more about the universe, this server provides the necessary tools to enhance your astronomical endeavors.