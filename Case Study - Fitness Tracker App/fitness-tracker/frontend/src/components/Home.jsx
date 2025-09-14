import { Link } from "react-router-dom";
import ft3 from "../images/ft5.jpg";
import ft4 from "../images/ft4.jpg";

export default function Home() {
  return (
    <div style={{ backgroundColor: "#000", color: "#fff", minHeight: "100vh" }}>
      <div className="container py-5">

        {/* Hero Section */}
        <div className="row align-items-center mb-5">
          <div className="col-md-6 d-flex justify-content-center">
            <img
              src={ft4}
              alt="Fitness"
              className="img-fluid rounded shadow-lg"
              style={{ maxHeight: "400px", objectFit: "cover" }}
            />
          </div>

          <div className="col-md-6 d-flex flex-column justify-content-center text-center text-md-start mt-4 mt-md-0">
            {/* Motivational Quote */}
            <h2
              style={{
                color: "#9929EA",
                fontWeight: "bold",
                fontStyle: "italic",
                textShadow: "2px 2px 5px rgba(0,0,0,0.5)",
                lineHeight: "1.4",
              }}
            >
              “Every step you take is a step closer to a healthier, stronger you.”
            </h2>

            {/* Subheading */}
            <h4
              className="mt-3"
              style={{
                color: "#D8BFD8",
                fontWeight: "600",
                letterSpacing: "1px",
              }}
            >
              Want to join? Just one step ahead!
            </h4>

            {/* Description */}
            <p className="mt-2" style={{ color: "#ccc" }}>
              Track your workouts, calories, and progress with ease.
            </p>

            {/* Buttons */}
            <div className="mt-4">
              <Link
                to="/login"
                className="btn me-3 px-4 py-2 shadow-sm"
                style={{
                  backgroundColor: "#9929EA",
                  color: "#fff",
                  borderRadius: "25px",
                  fontWeight: "600",
                  transition: "0.3s",
                }}
                onMouseEnter={(e) => (e.target.style.backgroundColor = "#7a1dbd")}
                onMouseLeave={(e) => (e.target.style.backgroundColor = "#9929EA")}
              >
                Login
              </Link>
              <Link
                to="/signup"
                className="btn px-4 py-2 shadow-sm"
                style={{
                  backgroundColor: "#9929EA",
                  color: "#fff",
                  borderRadius: "25px",
                  fontWeight: "600",
                  transition: "0.3s",
                }}
                onMouseEnter={(e) => (e.target.style.backgroundColor = "#7a1dbd")}
                onMouseLeave={(e) => (e.target.style.backgroundColor = "#9929EA")}
              >
                Signup
              </Link>
            </div>
          </div>
        </div>

        {/* About Section */}
        <div
          className="row align-items-center mb-5 p-4 rounded shadow-lg"
          style={{ backgroundColor: "#111", borderRadius: "20px" }}
        >
          <div className="col-md-6 order-md-2 d-flex justify-content-center mb-4 mb-md-0">
            <img
              src={ft3}
              alt="About"
              className="img-fluid rounded shadow"
              style={{ maxHeight: "450px", objectFit: "cover", width: "100%" }}
            />
          </div>

          <div className="col-md-6 order-md-1 text-center text-md-start">
            <h3
              style={{
                color: "#9929EA",
                fontWeight: "700",
                marginBottom: "20px",
                textShadow: "1px 1px 3px rgba(0,0,0,0.3)",
              }}
            >
              About Fitness Tracker
            </h3>
            <p style={{ color: "#ccc", lineHeight: "1.6", fontSize: "1.1rem" }}>
              Fitness Tracker helps you log your workouts, monitor calories,
              and visualize your progress with beautiful charts. Stay consistent,
              stay motivated, and achieve your fitness goals with us!
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
