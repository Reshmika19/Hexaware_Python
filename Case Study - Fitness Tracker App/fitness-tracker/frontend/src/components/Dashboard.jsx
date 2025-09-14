import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Footer from "../components/Footer";
import { FaDumbbell, FaChartLine, FaHeart, FaFire, FaWeight } from "react-icons/fa";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [workouts, setWorkouts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
      return;
    }

    fetch("http://127.0.0.1:5000/user/stats", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(res => res.json())
      .then(data => {
        setUser({ ...user, weight: data.weight });
        setWorkouts(Array(data.total_workouts).fill({ calories: data.total_calories / data.total_workouts || 0 }));
      })
      .catch(err => console.log(err));
  }, [navigate]);


  // Calculate total calories burned
  const totalCalories = workouts.reduce((sum, w) => sum + (w.calories || 0), 0);

  return (
    <div className="d-flex flex-column min-vh-100" style={{ backgroundColor: "#000", color: "white" }}>
      <div className="container flex-grow-1 py-5">
        {/* Welcome Section */}
        <div className="text-center mb-5">
          <h2 style={{ color: "#9929EA", fontFamily: "'Poppins', sans-serif", fontWeight: "700", textShadow: "2px 2px 8px rgba(153,41,234,0.5)" }}>
            Welcome {user ? user.name : "User"} 
          </h2>
          <p className="lead" style={{ color: "#ccc" }}>
            Track your fitness, workouts, and progress all in one place.
          </p>
        </div>

        {/* Dashboard Cards */}
        <div className="row text-center g-4 mb-5">
          <div className="col-md-4">
            <div
              className="card shadow-lg p-4 h-100 hover-glow"
              style={{ backgroundColor: "#1c1c1c", color: "white", cursor: "pointer", borderRadius: "15px" }}
              onClick={() => navigate("/workouts")}
            >
              <FaDumbbell size={40} color="#9929EA" className="mb-3" />
              <h4 style={{ color: "#9929EA", fontWeight: "600" }}>Manage Workouts</h4>
              <p style={{ color: "#bbb" }}>Log, edit, and view all your workouts easily.</p>
            </div>
          </div>

          <div className="col-md-4">
            <div
              className="card shadow-lg p-4 h-100 hover-glow"
              style={{ backgroundColor: "#1c1c1c", color: "white", cursor: "pointer", borderRadius: "15px" }}
              onClick={() => navigate("/analytics")}
            >
              <FaChartLine size={40} color="#9929EA" className="mb-3" />
              <h4 style={{ color: "#9929EA", fontWeight: "600" }}>View Progress</h4>
              <p style={{ color: "#bbb" }}>Check your calories burned and analytics charts.</p>
            </div>
          </div>

          <div className="col-md-4">
            <div
              className="card shadow-lg p-4 h-100 hover-glow"
              style={{ backgroundColor: "#1c1c1c", color: "white", cursor: "pointer", borderRadius: "15px" }}
              onClick={() => navigate("/profile")}
            >
              <FaHeart size={40} color="#9929EA" className="mb-3" />
              <h4 style={{ color: "#9929EA", fontWeight: "600" }}>Profile & Settings</h4>
              <p style={{ color: "#bbb" }}>Update your info and personalize your experience.</p>
            </div>
          </div>
        </div>

        {/* Quick Stats */}
        <div className="text-center mb-5">
          <h3 style={{ color: "#9929EA", fontWeight: "700", marginBottom: "20px" }}>Your Quick Stats</h3>
          <div className="row g-4 justify-content-center">
            <div className="col-md-3">
              <div className="card shadow-lg p-4 hover-glow" style={{ backgroundColor: "#1c1c1c", borderRadius: "15px" }}>
                <FaDumbbell size={30} color="#9929EA" className="mb-2" />
                <h5  style={{ color: "#bbb", fontWeight: "1000" }}>Total Workouts</h5>
                <p style={{ color: "#bbb", fontWeight: "600" }}>{workouts.length}</p>
              </div>
            </div>

            <div className="col-md-3">
              <div className="card shadow-lg p-4 hover-glow" style={{ backgroundColor: "#1c1c1c", borderRadius: "15px" }}>
                <FaFire size={30} color="#9929EA" className="mb-2" />
                <h5  style={{ color: "#bbb", fontWeight: "1000" }}>Calories Burned</h5>
                <p style={{ color: "#bbb", fontWeight: "600" }}>{totalCalories}</p>
              </div>
            </div>

            <div className="col-md-3">
              <div className="card shadow-lg p-4 hover-glow" style={{ backgroundColor: "#1c1c1c", borderRadius: "15px" }}>
                <FaWeight size={30} color="#9929EA" className="mb-2" />
                <h5  style={{ color: "#bbb", fontWeight: "1000" }} >Weight</h5>
                <p style={{ color: "#bbb", fontWeight: "600" }}>{user?.weight || 0} kg</p>
              </div>
            </div>
          </div>
        </div>

        {/* Motivational Quote */}
        <div className="mt-3 text-center">
          <h4 style={{ color: "#fff", fontStyle: "italic", textShadow: "1px 1px 4px rgba(153,41,234,0.5)" }}>
            “Consistency is what transforms average into excellence. Keep moving forward!”
          </h4>
        </div>
      </div>


      {/* Custom Hover Glow Style */}
      <style>
        {`
          .hover-glow:hover {
            box-shadow: 0 0 20px rgba(153, 41, 234, 0.6);
            transform: translateY(-5px);
            transition: all 0.3s ease;
          }
        `}
      </style>
    </div>
  );
}
