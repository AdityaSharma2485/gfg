class Solution {
  public:
    double findSmallestMaxDist(vector<int> &stations, int k) {
        int n = stations.size();
        double left = 0, right = stations[n-1] - stations[0];

        auto canPlaceStations = [&](double maxDist) {
            int neededStations = 0;
            for (int i = 1; i < n; ++i) {
                double dist = stations[i] - stations[i-1];
                neededStations += ceil(dist / maxDist) - 1;
            }
            return neededStations <= k;
        };

        while (right - left > 1e-6) {
            double mid = (left + right) / 2.0;
            if (canPlaceStations(mid)) {
                right = mid;
            } else {
                left = mid;
            }
        }

        return round(right * 100) / 100.0;
    }
};
