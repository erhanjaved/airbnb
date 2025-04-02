# Project Milestone 3
## Group AECA - Airbnb in NYC: Market Trends & Impact

### Erhan

#### **1. How does room type impact price variations?**

![Demo 1](../images/prelim_sketches/Erhan/q1.gif)

#### Design Goal:
This visualization was designed to explore how room types differ in pricing across New York and how these patterns vary by region. It aims to help users understand both the range and frequency of prices for each room type.

#### Visualization Approach:
We used a boxplot to show the distribution of prices for each room type, enhanced with an interactive custom legend. A histogram dynamically updates based on the selected room type, showing the full distribution of prices for that category.

#### Interactivity:
- A price slider filters listings to allow budget-focused exploration.
- A neighborhood dropdown filters data to specific boroughs or shows all at once.
- An interactive legend lets users click a room type to highlight it and grey out the others.
- A linked histogram updates in real time to reflect the room type selection, price filter, and neighborhood context.

#### Visualization Principles Applied:
- Marks: Box (boxplot), Bar (histogram), Point (legend)
- Channels: Position (for price and room type), Color (room type), Opacity (selection feedback)
- Channel Characteristics: Color effectively encodes nominal room types; position encodes price accurately; opacity is used to emphasize selection.

#### Critique:
The combination of multi-view coordination and filtering provides a strong exploratory tool. The interactive legend improves usability over a static one, and the histogram adds valuable detail beyond summary statistics. A small limitation is that the custom legend might not be immediately perceived as clickable. Including tooltips in the histogram could enhance usability further.

### **2. What is the effect of location (neighborhood group, latitude, and longitude) on price differences?**

![Demo 2](../images/prelim_sketches/Erhan/q2.gif)

#### Design Goal:
This view was designed to show how price varies by geography, helping users identify regional trends and compare neighborhoods spatially and statistically.

#### Visualization Approach:
A map of NYC listings was layered over real geographic boundaries. A bar chart shows the average price by borough. Both views are bidirectionally linked to provide a spatial and statistical lens into pricing.

#### Interactivity:
- A price slider filters listings on both the map and the bar chart.
- Users can click a borough in either the map or the chart to highlight it in both views.
- Bi-directional linking ensures greyed-out context for unselected regions while focusing the view.

#### Visualization Principles Applied:
- **Marks**: Circle (map), Bar (borough chart)
- **Channels**: Position (longitude/latitude, borough), Color (price), Size (fixed)
- **Channel Characteristics**: Spatial position reflects real geography; color conveys price; interaction highlights comparisons.

#### Critique:
The map and bar chart are well-coordinated, making exploration intuitive. The linked views encourage comparison and discovery. However, in high-density areas, overlapping points may obscure listings — clustering or aggregation could improve clarity.

### **3. Does the host's listing count or years of hosting (host_since) influence listing prices?**

![Demo 3](../images/prelim_sketches/Erhan/q3.gif)

#### Design Goal:
This visualization was designed to evaluate whether host experience or scale impacts Airbnb listing prices.

#### Visualization Approach:
A heatmap encodes average price based on host listing count and hosting experience. Users can adjust parameters to view different aggregations of price (mean, median, or max) and focus on hosts with a specific number of listings.

#### Interactivity:
- A price slider filters out high-end outliers.
- A host listing count slider allows focusing on individuals or commercial-scale hosts.
- A radio button allows switching between mean, median, or maximum prices.

#### Visualization Principles Applied:
- **Marks**: Rect
- **Channels**: Position (binned host experience and listing count), Color (aggregated price)
- **Channel Characteristics**: Color gradient reflects pricing differences; position allows multidimensional correlation.

#### Critique:
This chart is effective at showing large-scale patterns across host attributes. The color encoding supports rapid pattern detection. However, binning can flatten nuanced relationships, and adding tooltips or raw scatterplots could support deeper exploration.

### **4. How do reviews per month, review scores, and the total number of reviews correlate with pricing?**

![Demo 4](../images/prelim_sketches/Erhan/q4.gif)

#### Design Goal:
The goal here was to investigate whether review frequency and rating scores influence pricing trends across listings.

#### Visualization Approach:
A heatmap shows average price across binned review scores and reviews per month. Zooming and filtering allow users to explore patterns in trusted, frequently-reviewed listings.

#### Interactivity:
- A price slider filters out high-priced listings.
- A review count slider removes listings with minimal review data.
- Users can zoom and pan on the x-axis (reviews per month) for deeper inspection.
- Tooltips provide precise data for each bin.

#### Visualization Principles Applied:
- **Marks**: Rect
- **Channels**: Position (review score and frequency), Color (price)
- **Channel Characteristics**: Binning simplifies input space; color gradient allows comparison; tooltips aid in interpretation.

#### Critique:
The heatmap offers powerful pattern recognition, showing how price aligns with user feedback. However, the binning might obscure edge cases or small clusters. Additional views like scatterplots or density curves could complement this analysis.

### **5. What role does availability over 365 days and minimum nights play in pricing strategies?**

![Demo 5](../images/prelim_sketches/Erhan/q5.gif)

#### Design Goal:
This visualization was designed to reveal how minimum night requirements and availability influence pricing, particularly across different room types.

#### Visualization Approach:
Violin plots (constructed with `mark_area`) display the full distribution of prices across grouped minimum night ranges. The chart is faceted by room type and includes filters for price and room type.

#### Interactivity:
- A price slider allows users to focus on listings within a target range.
- A room type dropdown enables room-specific comparison or viewing all room types.
- The layout uses faceting and x-offset to clearly separate minimum night bins.

#### Visualization Principles Applied:
- **Marks**: Area (for violin plot)
- **Channels**: Position (price), Color (minimum night group), X-offset / Column (categorical faceting)
- **Channel Characteristics**: Area shape shows distribution density; position preserves detail; color distinguishes duration categories.

#### Critique:
The violin plots effectively communicate distribution spread and skewness, especially when faceted by room type. The custom binning of minimum nights helps interpret common booking behaviors. However, `mark_area` violins are less conventional, and adding a median line or sample size could help interpretation.