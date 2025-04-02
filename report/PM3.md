# Project Milestone 3
## Group AECA - Airbnb in NYC: Market Trends & Impact

### Erhan: Pricing & Affordability Trends

#### **1. How does room type impact price variations?**

![Demo 1](../images/prelim_sketches/Erhan/q1.gif)

**Design Goal:**  
This visualization was designed to explore how room types differ in pricing across New York and how these patterns vary by region. It aims to help users understand both the range and frequency of prices for each room type.

**Marks:**  
Box (Boxplot), Bar (Histogram), Point (Legend)

**Channels:**  
X-Position (Room Type), Y-Position (Price), Color Hue (Room Type), Opacity

**Characteristics of Channels that were exploited:**  
Position channels effectively encode categorical and quantitative variables—room types and prices, respectively. Color is used to distinguish room types, while opacity changes dynamically to draw focus to the selected type. The use of coordinated channels across the boxplot and histogram helps maintain cognitive continuity during interaction.

**Describe the interaction:**  
A price slider filters all views to focus on listings within a desired budget. A neighborhood dropdown allows users to isolate specific boroughs or compare all regions simultaneously. The custom interactive legend allows users to click a room type to highlight it while dimming the others. A linked histogram updates in real time based on room type selection and applied filters.

**Critique the view:**  
The visualization effectively combines summary statistics and full distributions through coordinated views. The interactive legend enhances user control and clarity. However, the legend may not be immediately perceived as clickable. Adding a default histogram view (when no room type is selected) or tooltip enhancements could further improve usability.


### **2. What is the effect of location (neighborhood group, latitude, and longitude) on price differences?**

![Demo 2](../images/prelim_sketches/Erhan/q2.gif)

**Design Goal:**  
This visualization was created to examine how Airbnb listing prices vary across NYC boroughs. It aims to help users identify regional pricing trends and make comparisons between neighborhoods through both spatial and statistical perspectives.

**Marks:**  
Circle (Map), Bar (Borough Chart)

**Channels:**  
Longitude/Latitude Position, Categorical X-Position, Color Hue, Size (Fixed)

**Characteristics of Channels that were exploited:**  
Color hue encoded price magnitude, allowing viewers to quickly identify higher and lower-priced areas. Geospatial positioning on the map reflected actual location, while x-position on the bar chart enabled categorical borough comparison. Color consistency across both views reinforced linking and aided interpretability.

**Describe the interaction:**  
When a borough is selected through clicking either the map or bar chart, it is highlighted across both views. Unselected areas are greyed out for context. A price slider further filters the listings displayed in both charts. This bi-directional interaction facilitates flexible, intuitive exploration from both geographic and quantitative entry points.

**Critique the view:**  
The map and bar chart function well together to support multi-angle comparison. The interactivity enhances usability and promotes deeper insight. However, listings in dense urban areas may visually overlap on the map, reducing clarity. Future iterations could incorporate aggregation techniques like hexbinning or spatial clustering to address this.


### **3. Does the host's listing count or years of hosting (host_since) influence listing prices?**

![Demo 3](../images/prelim_sketches/Erhan/q3.gif)

**Design Goal:**  
This visualization was designed to assess whether host experience and the number of listings a host manages influence Airbnb pricing. It supports exploration of how scale and tenure correlate with average price levels.

**Marks:**  
Rect

**Channels:**  
X-Position (Hosting Duration), Y-Position (Number of Listings), Color Hue

**Characteristics of Channels that were exploited:**  
Binned position channels were used to compare categories of host tenure and scale. Color hue encoded average price and highlighted pricing gradients across the 2D matrix. The combination of positional and color encoding enabled multi-dimensional comparisons in a compact format.

**Describe the interaction:**  
A price slider removes outliers, allowing a cleaner focus on typical pricing. A second slider restricts the number of listings to isolate small vs. large-scale hosts. A radio selection allows toggling between mean, median, or maximum pricing as the aggregation metric. These interactions provide analytical flexibility and support hypothesis-driven exploration.

**Critique the view:**  
The heatmap reveals general trends effectively and supports comparative analysis of host characteristics. The flexibility in aggregation is a strength. However, binning may obscure edge patterns or variability within each cell. Supplementing the heatmap with a scatterplot or tooltips could enhance interpretability.

### **4. How do reviews per month, review scores, and the total number of reviews correlate with pricing?**

![Demo 4](../images/prelim_sketches/Erhan/q4.gif)

**Design Goal:**  
This visualization was designed to explore whether review frequency and rating scores influence listing prices. It aims to uncover patterns that connect guest feedback metrics with pricing behavior on Airbnb.

**Marks:**  
Rect

**Channels:**  
X-Position (Reviews per Month), Y-Position (Review Scores), Color Hue

**Characteristics of Channels that were exploited:**  
Binning was used to group continuous variables into digestible segments. Color hue encoded average price and revealed pricing trends across review frequency and score combinations. Position channels helped distinguish the relationship between guest activity and listing valuation.

**Describe the interaction:**  
A price slider filters out expensive listings to focus on the general market. A review count slider removes low-signal listings. Users can pan and zoom along the reviews-per-month axis to inspect specific frequency ranges. Tooltips display exact values for detailed comparisons, supporting deeper investigation of each bin.

**Critique the view:**  
The heatmap effectively reveals how review behavior correlates with pricing. It’s especially strong in identifying sweet spots for high-rated, frequently-reviewed listings. However, some nuance is lost due to binning, and the view may underrepresent outliers or sparse bins. Supplementing with density plots or scatter overlays could address this limitation.

### **5. What role does availability over 365 days and minimum nights play in pricing strategies?**

![Demo 5](../images/prelim_sketches/Erhan/q5.gif)

**Design Goal:**  
This visualization was created to examine how pricing is influenced by listing availability and minimum night requirements, particularly across different room types. It aims to uncover distribution patterns that emerge under different booking constraints.

**Marks:**  
Area

**Channels:**  
Y-Position (Price), X-Offset / Column (Minimum Night Groups), Color Hue (Minimum Night Group)

**Characteristics of Channels that were exploited:**  
The area mark represents the density of prices within each minimum night group. Position encodes the distribution along the price axis, preserving variation and skew. Color distinguishes between minimum night categories, aiding comparison across bins. Faceting by room type introduces a third dimension, enabling segmented analysis.

**Describe the interaction:**  
A price slider filters out high-end listings to narrow the focus. A room type dropdown allows users to isolate specific room categories or view all simultaneously. Faceting separates room types into comparable columns, while x-offset organizes minimum night bins in a logical sequence.

**Critique the view:**  
The violin plots communicate pricing spread and shape effectively, particularly for identifying skew and variance. The layout supports comparison within and across room types. However, violin plots using `mark_area` may be unfamiliar to some viewers. Including median markers or frequency annotations could improve interpretability.

### Carol: Guest Experience & Satisfaction

#### **1. How do listing features like the number of amenities or instant booking availability impact guest satisfaction ratings?**

![Demo 1](../images/prelim_sketches/Carol/heatmap.gif)

**Design Goal:**  
This visualization helps explore how different listing features, like the number of amenities or instant booking, relate to guest satisfaction. It lets users see overall trends and dive deeper into specific features to understand their impact on different rating levels.

**Marks:**  
Rectangles (Heatmap), Bars (Bar Chart)

**Channels:**  
X-Position (Feature), Y-Position (Rating Bin), Color Hue (Correlation Strength)

**Characteristics of Channels that were exploited:**  
Position is used to organize features and rating bins, making it easy to compare correlations across different categories. Colour encodes correlation strength using a red-blue scale, allowing users to quickly spot positive and negative relationships. Sorting the bars in descending order ensures the strongest correlations are immediately visible.

**Describe the interaction:**  
A dropdown menu lets users switch between different rating types (e.g., overall rating, cleanliness, value). Clicking on a feature in the heatmap highlights its correlation values in the bar chart, showing how the feature is associated with guest satisfaction across different rating bins.

**Critique the view:**  
The visualization effectively summarizes complex relationships in a compact and interactive format. The heatmap provides an overview of correlations, while the linked bar chart allows for a deeper exploration of specific features. However, since correlation does not imply causation, some relationships may be misleading. Adding tooltips or explanatory text could help users interpret the data more accurately.

#### **2. What is the relationship between guest satisfaction ratings and the price of listings for different room types?**

![Demo 2](../images/prelim_sketches/Carol/scatterplot.gif)

**Design Goal:**  
This visualization examines the relationship between listing prices and guest satisfaction ratings across different room types. It helps users identify trends, such as whether higher-rated listings tend to be more expensive, and provides a clearer picture of the price distribution.

**Marks:**  
Circles (Scatter Plot), Bars (Histogram)

**Channels:**  
X-Position (Rating Score), Y-Position (Price), Color Hue (Room Type), Height (Listing Count in Histogram), Opacity

**Characteristics of Channels that were exploited:**  
Position effectively maps guest ratings against price, allowing users to see trends in how price impacts satisfaction. Colour differentiates room types, while opacity highlights selected categories. In the histogram, bar height represents the number of listings at different price points.

**Describe the interaction:**  
A price range slider filters both charts, helping users focus on specific price points. The interactive legend allows users to highlight particular room types, dimming the others for better visibility. 

**Critique the view:**  
The visualization highlights how price and ratings are connected while offering flexibility through interactive filters. However, the scatter plot can become cluttered in certain price ranges, making patterns harder to distinguish. Adding density contours or a smoothing technique could help clarify overlapping points.

#### **3. Which amenities are most frequently associated with higher guest ratings in Airbnb listings?**

![Demo 3](../images/prelim_sketches/Carol/dotplot.gif)

**Design Goal:**  
This visualization explores which amenities are most frequently linked to higher guest satisfaction in Airbnb listings. It allows users to compare correlations for all listings and highly-rated listings (ratings > 4.5) to see which amenities matter most.

**Marks:**  
Circles (Dot Plot), Text (Amenity List)

**Channels:**  
X-Position (Correlation Strength), Y-Position (Amenity), Color Hue (Listing Type), Opacity

**Characteristics of Channels that were exploited:**  
The position of each dot represents the correlation strength for each amenity. Colour differentiates between all listings and highly-rated listings, while opacity helps highlight selected amenities. The interactive text list also makes it easy to choose specific amenities.

**Describe the interaction:**  
A radio button lets users switch between all listings and highly-rated listings. Clicking an amenity in the list highlights its corresponding dot in the plot, and selecting a dot in the plot also highlights the corresponding text in the list, providing bidirectional linking. 

**Critique the view:**  
The visualization effectively highlights which amenities are associated with better guest ratings. However, since correlation does not imply causation, some amenities may appear important even if they don’t directly influence guest satisfaction. Additional analysis could help clarify whether these relationships are meaningful.
