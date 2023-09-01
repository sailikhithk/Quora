import React, { useState, useEffect } from "react";
import apiService from "../services/apiService";
import styled from "styled-components";

const ProfileContainer = styled.div`
  padding-left: 10%;
  padding-top: 20px;
  width: 80%;
`;

const ProfileImage = styled.img`
  width: 100px;
  height: 100px;
  border-radius: 50%;
`;

const ProfileForm = styled.form`
  display: flex;
  flex-direction: column;
`;

const InputField = styled.input`
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const SubmitButton = styled.button`
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  &:hover {
    background-color: #0056b3;
  }
`;

const Profile = () => {
  const [profile, setProfile] = useState({});
  const user_id = localStorage.getItem("user_id");

  useEffect(() => {
    // Fetch the user's profile details
    const fetchProfile = async () => {
      try {
        const response = await apiService.get(`/profile/${user_id}`);
        setProfile(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchProfile();
  }, [user_id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfile({
      ...profile,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Call the API to update the profile
    try {
      await apiService.put(`/profile/${user_id}`, profile);
      alert("Profile updated successfully!");
    } catch (error) {
      console.error(error);
      alert("An error occurred while updating the profile.");
    }
  };

  return (
    <ProfileContainer>
      <h2>Profile Settings</h2>
      <ProfileImage src={profile.image} alt="Profile" />
      <ProfileForm onSubmit={handleSubmit}>
        <InputField
          type="text"
          name="username"
          value={profile.username || ""}
          onChange={handleInputChange}
          placeholder="Username"
        />
        <InputField
          type="email"
          name="email"
          value={profile.email || ""}
          onChange={handleInputChange}
          placeholder="Email"
        />
        <SubmitButton type="submit">Update Profile</SubmitButton>
      </ProfileForm>
    </ProfileContainer>
  );
};

export default Profile;
