from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from barchart import plotly_bar_charts_3d
from barchart import verify_input


class TestInputValidation:
    """Test input validation logic"""

    def test_verify_input_valid_full_grid(self):
        """Test that full grid data passes validation"""
        x = [1, 2, 3]
        y = [4, 5]
        z = [10, 20, 30, 40, 50, 60]  # 3 * 2 = 6
        assert verify_input(x, y, z) is True

    def test_verify_input_valid_paired(self):
        """Test that paired data passes validation"""
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 30, 40, 50]
        z = [0.1, 0.2, 0.3, 0.4, 0.5]
        assert verify_input(x, y, z) is True

    def test_verify_input_invalid(self):
        """Test that invalid input raises ValueError"""
        x = [1, 2, 3]
        y = [4, 5]
        z = [10, 20, 30]  # Should be 6 values
        with pytest.raises(ValueError, match='Input arguments are not matching'):
            verify_input(x, y, z)


class TestDataTypeDetection:
    """Test that the main function correctly identifies data types"""

    def test_detects_full_grid_data(self):
        """Test detection of full grid data (CSV-like)"""
        # 3x3 grid with all 9 values
        x = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        y = [10, 20, 30, 10, 20, 30, 10, 20, 30]
        z = list(range(9))

        fig = plotly_bar_charts_3d(x, y, z)
        # Should create exactly 9 meshes for a 3x3 grid
        assert len(fig.data) == 9

    def test_detects_paired_data(self):
        """Test detection of paired coordinate data"""
        features = [2, 3, 5, 10, 20]
        neighbours = [31, 24, 10, 28, 48]
        accuracies = [0.9727, 0.9994, 0.9994, 0.9995, 0.9995]

        fig = plotly_bar_charts_3d(features, neighbours, accuracies)
        # Should create exactly 5 meshes for 5 data points
        assert len(fig.data) == 5

    def test_detects_sparse_array(self):
        """Test detection of sparse array data"""
        x = [1, 10]
        y = [2, 4]
        z = [10, 30, 20, 45]  # 2x2 = 4 values

        fig = plotly_bar_charts_3d(x, y, z)
        # Should create 4 meshes for a 2x2 sparse array
        assert len(fig.data) == 4


class TestBarPositioning:
    """Test that bars are positioned correctly"""

    def test_paired_data_positioning(self):
        """Test that paired data bars are at correct positions"""
        x_vals = [2, 5, 10]
        y_vals = [3, 7, 11]
        z_vals = [100, 200, 300]

        fig = plotly_bar_charts_3d(x_vals, y_vals, z_vals)

        # Check that we have 3 bars
        assert len(fig.data) == 3

        # Check x-axis labels match our unique values
        assert fig.layout.scene.xaxis.ticktext == ('2', '5', '10')
        assert fig.layout.scene.yaxis.ticktext == ('3', '7', '11')

        # Verify bar positions (they should be at 0, 2, 4 for 3 values)
        expected_x_positions = [0, 2, 4]
        expected_y_positions = [0, 2, 4]

        for i, mesh in enumerate(fig.data):
            # Each mesh has 8 vertices, first one gives us the position
            assert mesh.x[0] in expected_x_positions
            assert mesh.y[0] in expected_y_positions

    def test_sparse_array_grid_positioning(self):
        """Test sparse array creates proper grid"""
        x = [1, 10]
        y = [2, 4]
        z = [10, 30, 20, 45]

        fig = plotly_bar_charts_3d(x, y, z)

        # Should have 4 visible bars in a 2x2 grid
        visible_bars = [mesh for mesh in fig.data if mesh.opacity == 1]
        assert len(visible_bars) == 4

        # Collect positions
        positions = [(mesh.x[0], mesh.y[0]) for mesh in visible_bars]

        # Should have bars at all 4 grid positions
        expected_positions = {(0, 0), (2, 0), (0, 2), (2, 2)}
        assert set(positions) == expected_positions


class TestColorSchemes:
    """Test that color schemes work correctly"""

    def test_color_by_x(self):
        """Test coloring by x value"""
        x = [1, 1, 2, 2]
        y = [3, 4, 3, 4]
        z = [10, 20, 30, 40]

        fig = plotly_bar_charts_3d(x, y, z, color='x')

        # First two bars (same x) should have same color
        assert fig.data[0].color == fig.data[1].color
        # Third and fourth bars (different x) should have same color
        assert fig.data[2].color == fig.data[3].color
        # Different x values should have different colors
        assert fig.data[0].color != fig.data[2].color

    def test_color_by_y(self):
        """Test coloring by y value"""
        # Use a full grid data to properly test y coloring
        x = [1, 1, 2, 2]
        y = [3, 4, 3, 4]
        z = [10, 20, 30, 40]

        fig = plotly_bar_charts_3d(x, y, z, color='y')

        # For full grid data, bars are ordered by unique x values then unique y values
        # So with x=[1,2] and y=[3,4], the order is:
        # mesh[0]: x=1, y=3
        # mesh[1]: x=1, y=4
        # mesh[2]: x=2, y=3
        # mesh[3]: x=2, y=4
        colors = [mesh.color for mesh in fig.data]

        # Bars with y=3 (indices 0 and 2) should have same color
        assert colors[0] == colors[2]
        # Bars with y=4 (indices 1 and 3) should have same color
        assert colors[1] == colors[3]
        # Different y values should have different colors
        assert colors[0] != colors[1]

    def test_color_by_xy(self):
        """Test coloring by x+y (each bar different)"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        z = [10, 20, 30]

        fig = plotly_bar_charts_3d(x, y, z, color='x+y')

        # Each bar should have a different color
        colors = [mesh.color for mesh in fig.data]
        assert len(set(colors)) == 3


class TestArrayHandling:
    """Test handling of arrays"""

    def test_array_sparse(self):
        """Test sparse array"""
        xdf = pd.Series([1, 2, 3, 4])
        ydf = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        # Create sparse array with specific values
        z = np.array([[None] * 15 for i in range(4)])
        z[0, 6] = 64  # x=1, y=7
        z[0, 9] = 32  # x=1, y=10
        z[1, 8] = 38  # x=2, y=9
        z[1, 10] = 23  # x=2, y=11
        z[2, 10] = 65  # x=3, y=11
        z[2, 12] = 34  # x=3, y=13
        z[3, 12] = 20  # x=4, y=13
        z[3, 14] = 9  # x=4, y=15

        z_flat = z.flatten('F')
        zdf = pd.Series(z_flat)

        fig = plotly_bar_charts_3d(xdf, ydf, zdf, z_min=0)

        # Count visible bars (opacity = 1)
        visible_bars = [mesh for mesh in fig.data if mesh.opacity == 1]
        assert len(visible_bars) == 8  # Should have 8 visible bars

        # Check that we have the right number of visible bars
        # The specific positions depend on how the sparse array is interpreted
        # Just verify we have 8 non-None values that are visible
        z_values = [mesh.z[4] for mesh in visible_bars]  # z_max is at index 4
        expected_values = {64, 32, 38, 23, 65, 34, 20, 9}
        assert set(z_values) == expected_values


class TestAxisLabels:
    """Test that axis labels are set correctly"""

    def test_custom_axis_titles(self):
        """Test custom axis titles"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        z = [10, 20, 30]

        fig = plotly_bar_charts_3d(
            x, y, z, x_title='Features', y_title='Neighbours', z_title='Accuracy',
        )

        assert fig.layout.scene.xaxis.title.text == 'Features'
        assert fig.layout.scene.yaxis.title.text == 'Neighbours'
        assert fig.layout.scene.zaxis.title.text == 'Accuracy'

    def test_auto_legends(self):
        """Test automatic legend generation"""
        x = [10, 20, 30]
        y = [100, 200, 300]
        z = [1, 2, 3]

        fig = plotly_bar_charts_3d(x, y, z)

        # Should convert values to strings
        assert fig.layout.scene.xaxis.ticktext == ('10', '20', '30')
        assert fig.layout.scene.yaxis.ticktext == ('100', '200', '300')


class TestEdgeCases:
    """Test edge cases and special scenarios"""

    def test_single_bar(self):
        """Test with single bar"""
        x = [5]
        y = [10]
        z = [100]

        fig = plotly_bar_charts_3d(x, y, z)
        assert len(fig.data) == 1

    def test_with_pandas_series(self):
        """Test with pandas Series input"""
        x = pd.Series([1, 2, 3])
        y = pd.Series([4, 5, 6])
        z = pd.Series([10, 20, 30])

        fig = plotly_bar_charts_3d(x, y, z)
        assert len(fig.data) == 3

    def test_with_numpy_arrays(self):
        """Test with numpy array input"""
        x = np.array([1, 2, 3])
        y = np.array([4, 5, 6])
        z = np.array([10, 20, 30])

        fig = plotly_bar_charts_3d(x, y, z)
        assert len(fig.data) == 3

    def test_z_min_auto(self):
        """Test automatic z_min calculation"""
        x = [1, 2]
        y = [3, 4]
        z = [100, 200]

        fig = plotly_bar_charts_3d(x, y, z, z_min='auto')

        # z_min should be 0.8 * min(z) = 0.8 * 100 = 80
        expected_z_min = 80

        # Check that bars start at this z value
        for mesh in fig.data:
            assert min(mesh.z) == expected_z_min


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
