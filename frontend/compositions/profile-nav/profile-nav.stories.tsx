import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"
import ProfileNav from "./profile-nav"

export default {
  title: "Compositions/Profile Nav",
  component: ProfileNav
} as ComponentMeta<typeof ProfileNav>

const Template: ComponentStory<typeof ProfileNav> = (args) => <ProfileNav {...args} />

export const Default = Template.bind({})
Default.args = {}
