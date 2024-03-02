import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import { IoLeafOutline } from "react-icons/io5";
import "react-toastify/dist/ReactToastify.css";
import "./login.css";

const farmImage =
  "https://th.bing.com/th/id/OIG4.Fvx4ssFbMpgKm1j_7XEe?w=1024&h=1024&rs=1&pid=ImgDetMain";

const LoginForm = ({ setUserId, setRole }) => {
  const [loginFormData, setLoginFormData] = useState({
    username: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setLoginFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleLogin = async () => {
    if (!loginFormData.username || !loginFormData.password) {
      toast.error("Username and password are required");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("/user_login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: loginFormData.username,
          password: loginFormData.password,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setUserId(data.user_id);
        setRole(data.role);

        if (data.role === "Seller") {
          navigate(`/farmerdash`);
        } else if (data.role === "admin") {
          navigate(`/admin/*`);
        } else {
          navigate("/BuyerDash");
        }

        toast.success("Login successful!");
      } else {
        console.error("Server Error:", response.statusText);
        toast.error("An error occurred during login");
      }
    } catch (error) {
      console.error("Client Error:", error);
      toast.error("An error occurred during login");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-b from-white/70 via-green-400/50 to-blue-200/30">
      <div className="flex flex-col md:flex-row items-center justify-center w-full md:max-w-4xl bg-gradient-to-r from-white via-white to-green-500 shadow-lg rounded-lg overflow-hidden mt-8">
        <div
          className="w-full md:w-1/2 bg-cover bg-center h-80 rounded-lg"
          style={{ backgroundImage: `url(${farmImage})` }}
        />
        <div className="w-full md:w-1/2 py-4 px-4 md:py-6 md:px-6">
          <div className="flex items-center justify-center">
            <IoLeafOutline className="text-green-500 text-4xl" />
            <h1 className="text-3xl font-bold text-black ml-2">
              Agri-Soko Login
            </h1>
          </div>
          <div className="mt-6">
            <h2 className="text-2xl font-bold text-black mb-4 text-center">
              Login
            </h2>
            <ToastContainer />
            <form className="mt-4">
              <div className="mb-4">
                <label htmlFor="username" className="block text-gray-700">
                  Username:
                </label>
                <input
                  type="text"
                  id="username"
                  name="username"
                  value={loginFormData.username}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                  aria-label="Username"
                  required
                />
              </div>
              <div className="mb-6">
                <label htmlFor="password" className="block text-gray-700">
                  Password:
                </label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={loginFormData.password}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                  aria-label="Password"
                  required
                />
              </div>
              <button
                type="button"
                onClick={handleLogin}
                disabled={loading}
                className="w-full px-4 py-2 bg-green-800 text-white rounded-md hover:bg-green-600 focus:outline-none focus:bg-green-600"
              >
                {loading ? "Logging in..." : "Login"}
              </button>
            </form>
            <p className="mt-4 text-center">
              <Link
                to="/forgotpassword"
                className="text-blue-500 hover:underline"
              >
                Forgot Password
              </Link>
            </p>
            <p className="mt-4 text-center">
              Don't have an account?{" "}
              <Link to="/signup" className="text-blue-500 hover:underline">
                Sign up
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
