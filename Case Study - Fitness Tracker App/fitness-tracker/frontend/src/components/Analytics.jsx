import React, { useEffect, useState } from "react";
import Footer from "./Footer";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";
import { Pie, Bar as ChartBar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip as ChartTooltip,
  Legend as ChartLegend,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";
import { useNavigate } from "react-router-dom";

ChartJS.register(
  ArcElement,
  ChartTooltip,
  ChartLegend,
  CategoryScale,
  LinearScale,
  BarElement
);

const AnalyticsPage = () => {
  const navigate = useNavigate();
  const [filter, setFilter] = useState("5");
  const [analyticsGeneral, setAnalyticsGeneral] = useState(null);
  const [analyticsFiltered, setAnalyticsFiltered] = useState(null);

  const getDates = () => {
    const today = new Date();
    let startDate;
    if (filter === "3") startDate = new Date(today.setDate(today.getDate() - 3));
    else if (filter === "5") startDate = new Date(today.setDate(today.getDate() - 5));
    else startDate = new Date(today.getFullYear(), today.getMonth(), 1); // month
    return {
      start_date: startDate.toISOString().split("T")[0],
      end_date: new Date().toISOString().split("T")[0],
    };
  };

  const fetchAnalyticsGeneral = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;
    try {
      const res = await axios.get("http://127.0.0.1:5000/analytics", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setAnalyticsGeneral(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchAnalyticsFiltered = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;
    const { start_date, end_date } = getDates();
    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/progress/filter",
        { start_date, end_date },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      const totalWorkouts = res.data.length;
      const totalCalories = res.data.reduce((sum, w) => sum + w.calories, 0);
      const avgDuration = totalWorkouts
        ? res.data.reduce((sum, w) => sum + w.duration, 0) / totalWorkouts
        : 0;

      const caloriesPerTypeMap = {};
      res.data.forEach((w) => {
        if (!caloriesPerTypeMap[w.exercise_type]) caloriesPerTypeMap[w.exercise_type] = 0;
        caloriesPerTypeMap[w.exercise_type] += w.calories;
      });
      const caloriesPerType = Object.entries(caloriesPerTypeMap).map(([type, calories]) => ({
        exercise_type: type,
        calories,
      }));

      setAnalyticsFiltered({ totalWorkouts, totalCalories, avgDuration, caloriesPerType });
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchAnalyticsGeneral();
  }, []);

  useEffect(() => {
    fetchAnalyticsFiltered();
  }, [filter]);

  if (!analyticsGeneral || !analyticsFiltered)
    return <p className="text-center text-white mt-5">Loading analytics...</p>;

  const pieData = {
    labels: analyticsFiltered.caloriesPerType.map((c) => c.exercise_type),
    datasets: [
      {
        label: "Calories",
        data: analyticsFiltered.caloriesPerType.map((c) => c.calories),
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#8A2BE2", "#00FF7F"],
        borderWidth: 1,
      },
    ],
  };

  const barData = {
    labels: analyticsFiltered.caloriesPerType.map((c) => c.exercise_type),
    datasets: [
      {
        label: "Calories",
        data: analyticsFiltered.caloriesPerType.map((c) => c.calories),
        backgroundColor: "#9929EA",
      },
    ],
  };

  const durationData = analyticsGeneral.avg_duration_per_exercise.map((item) => ({
    name: item.exercise_type,
    Duration: parseFloat(item.avg_duration.toFixed(2)),
  }));

  return (
    <div style={{ backgroundColor: "#000", color: "#fff", minHeight: "100vh", padding: "20px" }}>
      {/* Back Button */}
      <button
        className="btn btn-theme mb-4"
        style={{ marginBottom: "20px" }}
        onClick={() => navigate("/dashboard")}
      >
        Back to Dashboard
      </button>

      <h2 className="mb-4" style={{ color: "#9929EA" }}>
        Analytics Dashboard
      </h2>

      {/* General KPIs */}
      <div className="row mb-5">
        {[
          { title: "Total Calories This Week", value: analyticsGeneral.total_week_calories + " kcal" },
          { title: "Total Calories This Month", value: analyticsGeneral.total_month_calories + " kcal" },
          { title: "Max Calories in Single Workout", value: analyticsGeneral.max_calories_single_workout + " kcal" },
        ].map((item, idx) => (
          <div key={idx} className="col-md-4 mb-3">
            <div className="p-4 rounded shadow-lg" style={{ backgroundColor: "#111", boxShadow: "0 0 15px #9929EA" }}>
              <h5>{item.title}</h5>
              <p style={{ fontSize: "1.5rem" }}>{item.value}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Duration Chart */}
      <div className="mb-5 p-3 rounded shadow-lg" style={{ backgroundColor: "#111", boxShadow: "0 0 15px #9929EA" }}>
        <h4 style={{ color: "#9929EA" }}>Average Duration per Exercise</h4>
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={durationData} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#444" />
            <XAxis dataKey="name" stroke="#fff" />
            <YAxis stroke="#fff" />
            <Tooltip />
            <Legend />
            <Bar dataKey="Duration" fill="#EA29B0" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Filter Dropdown */}
      <div className="mb-4">
        <label className="form-label">Select Period: </label>
        <select
          className="form-select w-auto d-inline-block ms-2 theme-input"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option value="3">Last 3 Days</option>
          <option value="5">Last 5 Days</option>
          <option value="month">This Month</option>
        </select>
      </div>

      {/* Filtered KPIs */}
      <div className="d-flex flex-wrap gap-3 mb-4">
        {[
          { title: "Total Workouts", value: analyticsFiltered.totalWorkouts },
          { title: "Total Calories", value: analyticsFiltered.totalCalories + " kcal" },
          { title: "Average Duration", value: analyticsFiltered.avgDuration.toFixed(1) + " mins" },
        ].map((item, idx) => (
          <div key={idx} className="p-3 rounded shadow-lg" style={{ background: "#111", flex: "1 1 200px", boxShadow: "0 0 10px #9929EA" }}>
            <h5>{item.title}</h5>
            <h3>{item.value}</h3>
          </div>
        ))}
      </div>

      {/* Charts */}
      <div className="row">
        <div className="col-md-6 mb-4 p-3 rounded shadow-lg" style={{ background: "#111", boxShadow: "0 0 15px #9929EA" }}>
          <h5>Calories per Exercise Type (Pie Chart)</h5>
          <div style={{ height: "650px", width: "100%" }}>
            <Pie data={pieData} />
          </div>
        </div>
        <div className="col-md-6 mb-4 p-3 rounded shadow-lg" style={{ background: "#111", boxShadow: "0 0 15px #9929EA" }}>
          <h5>Calories per Exercise Type (Bar Chart)</h5>
          <ChartBar
            data={barData}
            options={{ plugins: { legend: { display: false } } }}
            height={250}
          />
        </div>
      </div>

    </div>
  );
};

export default AnalyticsPage;
