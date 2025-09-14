export default function Footer() {
  return (
    <footer 
      className="text-center py-4 mt-auto" 
      style={{ 
        borderTop: "1px solid #444", 
        backgroundColor: "#0d0d0d", 
        color: "white", 
        fontFamily: "'Poppins', sans-serif",
        boxShadow: "0 -2px 10px rgba(153, 41, 234, 0.3)"
      }}
    >
      <p style={{ margin: 0, fontWeight: "500" }}>
        © 2025 <span style={{ color: "#9929EA", fontWeight: "700" }}>Fitness Tracker</span>
      </p>
      <p style={{ margin: 0, fontSize: "0.85rem", color: "#bbb" }}>
        Made with ❤️ to keep you fit!
      </p>
    </footer>
  );
}
